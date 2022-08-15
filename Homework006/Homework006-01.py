# 1- Определить, присутствует ли в заданном списке строк, некоторое число
# 2- Найти сумму чисел списка стоящих на нечетной позиции
# 3- Найти расстояние между двумя точками пространства(числа вводятся через пробел)
# 4- Определить, позицию второго вхождения строки в списке либо сообщить, что её нет.
# Примеры
# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1
# 5- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# 6-Сформировать список из  N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

# 1 задача

list_of_str = ['sfg234w', 'awert43awsd', 'qd1v3q5637a', 'lkj1213fk', 'sdf13vbn']
def is_num_in_list(num: int, lst: list):
    # return True if (filter(lambda line: str(num) in line, lst)) else False   # Это почему-то не работает, всегда выдает True
    return list(filter(lambda line: str(num) in line, lst))
    # или:
def is_num_in_list(num: int, lst: list):
    res = list(filter(lambda line: str(num) in line, lst))
    if len(res) != 0:
        return (f"Число {num} присутствует в списке строк")
    else:
        return (f"Число {num} не присутствует в списке строк")
print(is_num_in_list(13, list_of_str))


# 2 задача
#
from functools import reduce

list_of_num = [1, 2, 3, 3, 4, 4, 5, 6, 7, 8, 9, 10]
def sum_of_odd_elem(lst: list):
    return reduce(lambda x, y: x + y, lst[1::2])
print(sum_of_odd_elem(list_of_num))


# 3 задача

def DistPoints(Ax, Ay, Bx, By):
    return ((Bx - Ax) ** 2 + (By - Ay) ** 2) ** 0.5
Ax, Ay, Bx, By = map(float, input('Введите координаты точек А и B (Ax, Ay, Bx, By) через пробел: ').split())
print(DistPoints(Ax, Ay, Bx, By))


# 4 задача

lst = ["qwe", "asd", "zxc", "qwe", "ertqwe"]
def sec_entry(lst: list, elem: str):
    return [i for i, elt in enumerate(lst) if elem in elt][1] if len([i for i, elt in enumerate(lst)]) >= 2 else 'Второго вхождения нет'
print(sec_entry(lst, 'qwe'))


# 5 задача

import random
from math import ceil
def pair_mult():
    N = int(input('Ведите количество элементов списка: '))
    min = int(input('Ведите минимальное число в списке чисел: '))
    max = int(input('Ведите максимальное число в списке чисел: '))
    num_list = [random.randint(min, max) for i in range(N)]
    print(num_list)
    return [num_list[i] * num_list[-i-1] for i in range(ceil(len(num_list) / 2))]
print(pair_mult())


# 6 задача

def list_of_seq():
    N = int(input('Введите количество элементов: '))
    return [(-3) ** i for i in range(1, N+1)]
print(list_of_seq())
