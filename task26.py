# Задача 26:  Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.
#
# *Пример:*
#
# A = 3; B = 5 -> 243 (3⁵)
#     A = 2; B = 3 -> 8
result = 1
def input_num(mesage: str):
    while True:
        numb = input(mesage)
        if numb.isdigit():
            return int(numb)

def sqrtt(number_1: int, number_2: int, result: int):
    if number_2 == 0:
        return result
    else:
        result *= number_1
        return sqrtt(number_1,number_2-1,result)

num = input_num('Введите число для возведения в степень: ')
sqrt = input_num('Введите степень: ')


print(sqrtt(num,sqrt,result))