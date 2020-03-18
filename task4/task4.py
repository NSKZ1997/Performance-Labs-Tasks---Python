#Задание #4 (task #4)
def check_strings(string1, string2):
    identical = True
    min_length = min(len(string1), len(string2)) - 1
    for i in range(min_length): #<-- Проверяет все буквы, кроме последней.
        if string1[i] != string2[i] and string2[i] != "*":
            identical = False
    if string2[-1] != '*' or (string1[min_length] != string2[min_length] and string2[min_length] != '*'):
        identical = False #<-- Проверяет последнюю букву.
    return identical

result = check_strings("yes", "yen") #<--- Вводить строки сюда.

if result:
    print('OK')
else:
    print('KO')