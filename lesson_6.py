from modul1 import check_data_view
from sys import argv
import random


if __name__ == '__main__':
    # test = input('Введите год в виде DD.MM.YYYY ==> ')
    check_data_view(argv[1])

# Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга. Вам дана расстановка 8 ферзей на доске,
# определите, есть ли среди них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.


N = 8
x = []
y = []


def inp():
    for i in range(N):
        new_x, new_y = [int(s) for s in input(f'введите {i + 1} пару чисел на доске 8×8, через пробел:').split()]
        x.append(new_x)
        y.append(new_y)


def check(x1, y1):
    correct = True
    for i in range(N):
        for j in range(i + 1, N):
            if x1[i] == x1[j] or y1[i] == y1[j] or abs(x1[i] - x1[j]) == abs(y1[i] - y1[j]):
                correct = False

    if correct is True:
        return False
    else:
        return True

if __name__ == '__main__':
    inp()
    print(x)
    print(y)
    # print(check(x, y))



# Напишите функцию в шахматный модуль. Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки. *Выведите все успешные вариа нты расстановок

BOARD_SIZE = 8
SIZE = 100


def rand(size):
    res = []
    i = 0
    while i < size:
        gen = [random.randint(0, size), random.randint(0, size)]
        i += 1
        if gen in res:
            i -= 1
        else:
            res.append(gen)
    return res

def my_func():
    count = 0
    count_tryes = 0
    while count < SIZE:
        count_tryes += 1
        t_qeen_list = rand(BOARD_SIZE)
        t = list(t_qeen_list)
        new_x, new_y = map(list, zip(*t_qeen_list))
        if check(new_x, new_y):
            print(t_qeen_list, count_tryes)
            count += 1


if __name__ == '__main__':
    my_func()