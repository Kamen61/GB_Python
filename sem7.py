# ✔ Напишите функцию, которая заполняет файл
# (добавляет в конец) случайными парами чисел.
# ✔ Первое число int, второе - float разделены вертикальной чертой.
# ✔ Минимальное число - -1000, максимальное - +1000.
# ✔ Количество строк и имя файла передаются как аргументы функции
import os
from pathlib import Path
from random import randint, uniform, choice


def fun1(count_str: int, file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        for i in range(count_str):
            print(f'{randint(-1000, 1000)}|{uniform(-1000, 1000)}', file=f)


# ✔ Напишите функцию, которая генерирует
# псевдоимена.
# ✔ Имя должно начинаться с заглавной буквы,
# состоять из 4-7 букв, среди которых
# обязательно должны быть гласные.
# ✔ Полученные имена сохраните в файл.


def fun2(file_name: str):
    with open(file_name, 'w', encoding='utf-8') as f:
        lenght = randint(4, 7)
        word = ''
        glas = (97, 101, 117, 105, 111)
        check = False
        for i in range(lenght):
            letrs = randint(97, 122)
            word += chr(letrs)
            if letrs in glas:
                check = True
        if not check:
            word = word.replace(choice(word), chr(choice(glas)), 1)
        print(word.capitalize(), file=f)


# fun1(10,'text.txt')
# fun2('text22.txt')


# ✔ Напишите функцию, которая открывает на чтение созданные
# в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните
# имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя
# записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя
# прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк,
# сколько в более длинном файле.
# ✔ При достижении конца более короткого файла,
# возвращайтесь в его начало.

# def fun3(file1, file2, file3):
#     with open(file1, 'r', encoding='utf-8') as f1, \
#             open(file2, 'r', encoding='utf-8') as f2, \
#                 open(file3, 'w', encoding='utf-8') as f3:
#         word = f2.readline()
#
#         while res := f1.readline():
#             nums = res.split('|')
#             nums = int(nums[0])* float(nums[1])
#             if nums > 0:
#                 res = f'{word.strip().lower()} {round(nums)}'
#             else:
#                 res = f'{word.strip().upper()} {abs(nums)}'
#             print(res,file=f3)
#
# fun3('text.txt', 'text22.txt', 'text3.txt')


# ✔ Создайте функцию, которая создаёт файлы с указанным расширением.
# Функция принимает следующие параметры:
# ✔ расширение
# ✔ минимальная длина случайно сгенерированного имени, по умолчанию 6
# ✔ максимальная длина случайно сгенерированного имени, по умолчанию 30
# ✔ минимальное число случайных байт, записанных в файл, по умолчанию 256
# ✔ максимальное число случайных байт, записанных в файл, по умолчанию 4096
# ✔ количество файлов, по умолчанию 42
# ✔ Имя файла и его размер должны быть в рамках переданного диапазона.


def fun4(extension, min_len=6, max_len=30, min_bits=256, max_bits=4096, amount_file=42, directory=None):
    if directory is None:
        directory = os.getcwd()
    amount_file = abs(amount_file)
    lst_file_name_in_directory = os.listdir()
    while amount_file:
        len_name_file = randint(min_len, max_len)
        amount_bits = randint(min_bits, max_bits)
        name = "".join([chr(randint(97, 122)) for i in range(len_name_file)])
        file_name = f'{name}.{extension}'
        if file_name not in lst_file_name_in_directory:
            with open(file_name, 'w', encoding='utf-8') as f:
                for i in range(amount_bits):
                    print(chr(randint(97, 122)), file=f, end='')
            amount_file -= 1


# fun4('py', amount_file=2)

# ✔ Доработаем предыдущую задачу.
# ✔ Создайте новую функцию которая генерирует файлы с разными расширениями.
# ✔ Расширения и количество файлов функция принимает в качестве параметров.
# ✔ Количество переданных расширений может быть любым.
# ✔ Количество файлов для каждого расширения различно.
# ✔ Внутри используйте вызов функции из прошлой задачи.


def fun5(extension_and_amount_files: dict):
    for key, values in extension_and_amount_files.items():
        fun4(key, amount_file=values)


# fun5({'py':2,'txt':2})


# ✔ Дорабатываем функции из предыдущих задач.
# ✔ Генерируйте файлы в указанную директорию — отдельный параметр функции.
# ✔ Отсутствие/наличие директории не должно вызывать ошибок в работе функции
# (добавьте проверки).
# ✔ Существующие файлы не должны удаляться/изменяться в случае совпадения имён

# def fun6(extension_and_amount_files: dict, directory=None):
#     for key, values in extension_and_amount_files.items():
#         fun4(key, amount_file=values, directory=directory)
#
# fun6({'py':2,'txt':2})

# Задание №7
# ✔ Создайте функцию для сортировки файлов по директориям: видео, изображения, текст и т.п.
# ✔ Каждая группа включает файлы с несколькими расширениями.
# ✔ В исходной папке должны остаться только те файлы, которые не подошли для сортировки.

def fun7(lst_extension: list):
    files = [i for i in os.listdir() if not os.path.isdir(i) and i.split('.')[1] in lst_extension]
    for i in files:
        extens = i.split('.')
        if extens[1] not in os.listdir():
            os.mkdir(extens[1])
        file = Path(i)
        file.replace(Path.cwd()/extens[1]/file)

fun7(['py','txt'])