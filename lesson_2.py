# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

# def fun_hex(num):
#     result = ''
#     while num:
#         result=str(num%16)+result
#         num//=16
#     return '0x'+result
# print(fun_hex(333))
# print(hex(333))


# def print_hex(a_input):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Вы ввели {a_input}\n')  # Press Ctrl+F8 to toggle the breakpoint.
#     dict_hex = {10: 'A',
#                 11: 'B',
#                 12: 'C',
#                 13: 'D',
#                 14: 'E',
#                 15: 'F'}
#     a = a_input
#     result = ''
#     while (a // 16) > 0:
#         ostatok = a % 16
#         if ostatok > 9:
#             result= dict_hex[ostatok] + result
#         else:
#             result= str(ostatok) + result
#
#         a = a // 16
#     result = str(a) + result
#
#     print(f'Число {a_input} в шестнатиричной системе => {("".join(result))}')
#     print(f'Проверка: {a_input} в шестнатиричной системе => {hex(a_input)}')
#
#
#
# a = -1
# while a < 0 or a > 1000000:
#     try:
#         a = int(input('Введите a от 1 до 1000000 => '))
#     except:
#         print('Введите число')
# print_hex(a)

# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.


frac_1 = input('Введите первую дробь')
frac_2 = input('Введите вторую дробь')


def translate(frac):
    numerator, denominator = frac.split('/')
    return int(numerator), int(denominator)


def nod(num_1, num_2):
    while num_1 and num_2:
        if num_1 > num_2:
            num_1 = num_1 % num_2
        else:
            num_2 = num_2 % num_1
    return num_1 + num_2

def output (num_1,num_2):
    return f'{num_1} / {num_2}'

def mult(frac_1, frac_2):
    num1_numerator, num1_denominator = translate(frac_1)
    num2_numerator, num2_denominator = translate(frac_2)
    numerator = num1_numerator * num2_numerator
    denominator = num1_denominator * num2_denominator
    reduction = nod(numerator, denominator)
    return output(numerator / reduction, denominator / reduction)


def sum(frac_1, frac_2):
    num1 = translate(frac_1)
    num2 = translate(frac_2)
    if num1[1] == num2[1]:
        numerator = num1[0] + num2[0]
        denominator = num1[1]
    elif not max(num1[1], num2[1]) % min(num1[1], num2[1]):
        numerator = (max(num1[1], num2[1]) / num1[1] * num1[0]) + (max(num1[1], num2[1]) / num2[1] * num2[0])
        denominator = max(num1[1], num2[1])
    else:
        denominator = num1[1] * num2[1]
        numerator = num1[0] * num2[1] + num2[0] * num1[1]
    reduction = nod(numerator, denominator)
    return output(numerator / reduction, denominator / reduction)


print(f'умножение дробей : {mult(frac_1, frac_2)}')
print(f'cложение дробей : {sum(frac_1, frac_2)}')
