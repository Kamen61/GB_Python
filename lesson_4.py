# ✔ Напишите функцию для транспонирования матрицы
#
# def fun(matrx):
#     res=[[0 for _ in range(len(matrx))] for _ in range(len(matrx[0]))]
#
#     for i in range(len(matrx)):
#         for j in range(len(matrx[0])):
#             res[j][i]=matrx[i][j]
#
#     return res



# ✔ Напишите функцию принимающую на вход только ключевые
# параметры и возвращающую словарь, где ключ — значение
# переданного аргумента, а значение — имя аргумента. Если
# ключ не хешируем, используйте его строковое представление.

# from collections.abc import Hashable
#
# def fun(**kwargs):
#     dic={}
#     for i,j in kwargs.items():
#         if not isinstance(j,Hashable):
#             dic[i]=str(j)
#         else:
#             dic[i]=j
#     return dic


