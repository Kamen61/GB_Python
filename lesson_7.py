# Напишите функцию группового переименования файлов. Она должна:
# принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
# принимать параметр количество цифр в порядковом номере.
# принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
# принимать параметр расширение конечного файла.
# принимать диапазон сохраняемого оригинального имени.
#
# Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
# К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
import os
import random
from typing import Tuple


def replace_name_file(file_name, amount_nums_in_name, extension, ending_extension, len_name_file: Tuple[int,int]):
    for j in os.listdir():
        lst_file_name = j.split('.')
        if len(lst_file_name) > 1 and lst_file_name[1] in extension:
            serial_number = "".join([str(random.randint(1, 9)) for i in range(amount_nums_in_name)])
            gen_file_name = lst_file_name[0][len_name_file[0]:len_name_file[1] + 1] + \
                            file_name + serial_number + '.' + ending_extension
            os.rename(j,gen_file_name)


# replace_name_file('qwe', 3, 'txt', 'py', (2,3))



# 2.Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами.
