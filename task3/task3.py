#Задание #3 (task #3)
import datetime
import time
import re

def timestamp_to_seconds(input_string, delimiters):
    pattern = '|'.join(map(re.escape, delimiters))
    time_stamp = re.split(pattern, input_string)
    if time_stamp[-1] == "": time_stamp = time_stamp[0:-1]
    year = int(time_stamp[0])
    month = int(time_stamp[1])
    day = int(time_stamp[2])
    hour = int(time_stamp[3])
    minute = int(time_stamp[4])
    second = int(time_stamp[5])
    millisecond = int(time_stamp[6])/1000
    current_time = datetime.datetime(year, month, day, hour, minute, second)
    current_time = time.mktime(current_time.timetuple()) + millisecond
    return current_time

class Log_reader:
    def __init__(self):
        self.delimiters = "-", "Т", "T", "Z", ":", "."
        self.len_timestring = len("2020-01-01Т12:51:32.124Z")
    
    def parse(self, filepath, start_time, end_time):
        
        self.success_count = 0
        self.fail_count = 0
        self.success_amount_top_up = 0
        self.success_amount_scoop = 0
        self.fail_amount_top_up = 0
        self.fail_amount_scoop = 0
        
        with open(filepath, 'r', encoding="utf8") as f:
            data = f.read().splitlines()
            len_str1 = len(data[1]) - len(" (объем бочки)")
            self.barrel_volume = int(data[1][:len_str1])
            len_str2 = len(data[2]) - len(" (текущий объем воды в бочке)")
            self.current_volume = int(data[2][:len_str2])
            self.volume_start = self.current_volume
            self.volume_end = self.current_volume
            try:
                start_time_seconds = timestamp_to_seconds(start_time, self.delimiters)
                end_time_seconds = timestamp_to_seconds(end_time, self.delimiters)
            except:
                print("usage") #Так нужно делать, если аргументы поданы не правильно?
                return None
            for line in data[3:]:
                useful_data = line.split(' ')
                if useful_data[0][-1] == 'Z': #Чтобы программа не крашилась, если формат времени не опознан, оно будет считаться как как в пределах нашего промежутка. 
                    current_time_seconds = timestamp_to_seconds(line[0:self.len_timestring], self.delimiters)
                else: 
                    current_time_seconds = end_time_seconds
                if current_time_seconds < start_time_seconds:
                    break #Прекрашаем итерацию если уже смотриться раньше указанного периода (так быстрее работает).
                
                if useful_data[-1] == '(успех)':
                    amount = int(useful_data[-2][:-1])
                    if useful_data[-3] == 'up':
                        self.volume_start -= amount
                        if current_time_seconds > end_time_seconds:
                            self.volume_end -= amount
                    elif useful_data[-3] == 'scoop':
                        self.volume_start += amount
                        if current_time_seconds > end_time_seconds:
                            self.volume_end += amount
                
                if current_time_seconds <= end_time_seconds:
                    if useful_data[-1] == '(успех)':
                        self.success_count += 1
                        amount = int(useful_data[-2][:-1])
                        if useful_data[-3] == 'up':
                            self.success_amount_top_up += amount
                        elif useful_data[-3] == 'scoop':
                            self.success_amount_scoop += amount
                    elif useful_data[-1] == '(фейл)':
                        self.fail_count += 1
                        amount = int(useful_data[-2][:-1])
                        if useful_data[-3] == 'up':
                            self.fail_amount_top_up += amount
                        elif useful_data[-3] == 'scoop':
                            self.fail_amount_scoop += amount
                            
            
            
            self.total_count = self.success_count + self.fail_count
            print("Количество попыток за указанный период: " + str(self.total_count))
            print("Процент ошибок = "+ str(round(self.success_count/(self.total_count) * 100)) + "%")
            print("Обьем воды налит за указанный переод: " + str(self.success_amount_top_up) + " литров")
            print("Обьем воды не налит за указанный переод: " + str(self.fail_amount_top_up) + " литров")
            print("Обьем воды извлеченно за указанный переод: " + str(self.success_amount_scoop) + " литров")
            print("Обьем воды не извлеченно за указанный переод: " + str(self.fail_amount_scoop) + " литров")
            print("Обьем воды в начале заданного переуда: " + str(self.volume_start) + " литров")
            print("Обьем воды в конце заданного переуда: " + str(self.volume_end) + " литров")
            
        
log = Log_reader()
log.parse('log_file.csv', '2020-01-01Т12:51:32.124', '2020-01-01Т12:51:34.769')