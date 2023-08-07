'''
Создайте класс студента. Используя дескрипторы проверяйте ФИО на первую заглавную букву
и наличие только букв. Названия предметов должны загружаться из файла CSV при создании экземпляра.
Другие предметы в экземпляре недопустимы. Для каждого предмета можно хранить оценки (от 2 до 5) и
результаты тестов (от 0 до 100). Также экземпляр должен сообщать средний балл по тестам для каждого
предмета и по оценкам всех предметов вместе взятых.
'''

import csv


class Capitalize:
    '''Проверка на заглавные буквы'''

    def check(self, value: str):
        '''Проверка'''
        if value != value.capitalize() or not value.isalpha():
            raise TypeError(
                'Строка должна начинаться с заглавной буквы и содержать только буквы')

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.check(value)
        setattr(instance, self.name, value)


class Student:
    firstname = Capitalize()
    lastname = Capitalize()
    patronim = Capitalize()

    def __init__(self, firstname, lastname, patronim) -> None:
        self.firstname = firstname
        self.lastname = lastname
        self.patronim = patronim

    def cal_average(self):
        '''Вычисление средней оценки'''
        dict_average = {}  # Словарь средних оценок
        with open('lessons.csv', 'r', encoding='utf-8', newline='') as r_file:
            filereader = csv.DictReader(r_file, delimiter=';')
            for line in filereader:
                grades = list(map(int, line['Grades'].split()))
                tests = list(map(int, line['Tests'].split()))
                av_grades = sum(grades) / len(grades) #средняя оценка
                av_tests = sum(tests) / len(tests) #средний балл
                dict_average[line['Lesson']] = (
                    '%.2f' % av_grades, '%.2f' % av_tests)

        for k, v in dict_average.items():
            print(
                f'Предмет: {k}, средняя оценка: {v[0]}, средний балл теста: {v[1]}')

        sum_grades = sum([float(k[0]) for _, k in dict_average.items()])
        sum_test = sum([float(k[1]) for _, k in dict_average.items()])

        print("Средняя оценка по всем предметам:", '%.2f' % (sum_grades / len(dict_average)),
              "Средний балл по всем тестам:", '%.2f' % (sum_test / len(dict_average)))


stud_1 = Student('Valet', 'Filimonov', 'Gavrilovich')
print(stud_1.__dict__, stud_1.firstname)
stud_1.cal_average()
