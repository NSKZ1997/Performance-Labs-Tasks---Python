#Задание #1 (task #1)
import math
#Сначало, читаем и сортируем массив данных. Примерный массив включён в папке этого задание.

with open('sample_database1.txt', 'r') as f:
    database1 = f.read().splitlines()

for i in range(len(database1)): #<-- Конвертивуем стринги в флоаты.
    database1[i] = int(database1[i])

def sort_database(alist): #<-- В Python Можно всё сортировать используя функцию .sort но это не интересно.
    sorted_database = []
    while alist:
        minimum = alist[0]
        for i in alist:
            if i < minimum:
                minimum = i
        sorted_database.append(minimum)
        alist.remove(minimum)
    return sorted_database

def get_percentile(alist, percentile): #<--- Фунция, которая определяет где находиться среднее число, перцентильное, и вычисляеться сумма.
    len_list = len(alist)
    percentile_index = math.ceil((percentile/100)*len_list)
    average_index = math.floor(len_list/2)
    
    new_list = alist[average_index:percentile_index]
    return sum(new_list)
    
database1 = sort_database(database1)
answer = get_percentile(database1, 90)
print('Сумма: ' + str(answer))