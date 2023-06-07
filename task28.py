# Задача 28: Напишите рекурсивную функцию sum(a, b),
# возвращающую сумму двух целых неотрицательных чисел.
# Из всех арифметических операций допускаются только +1 и -1.
# Также нельзя использовать циклы.
#
# *Пример:*
#
# 2 2
#     4

def input_num(mesage: str):
    while True:
        numb = input(mesage)
        if numb.isdigit():
            return int(numb)

def sqrtt(number_1: int, number_2: int):
    if number_2 == 0:
        return number_1
    else:
        return sqrtt(number_1 + 1,number_2 -1)

num = input_num('Введите первое число: ')
num_2 = input_num('Введите второе число: ')
print(sqrtt(num,num_2))