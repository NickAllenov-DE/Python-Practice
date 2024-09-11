# 2 - Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# *Пример:*
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

import random as rd

size = int(input('Выберите количество элементов в списке: '))
userlist = list(rd.randint(-10, 10) for i in range(size))
print(userlist)

def mult_of_pairs(a: list):
    ''' программа найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.'''

    if len(a) % 2:
        halfa = len(a) // 2 + 1
    else:
        halfa = len(a) // 2

    newlist = []
    for i in range(halfa):
        mult = a[i] * a[(size-1)-i]
        newlist.append(mult)

    return newlist

print(mult_of_pairs(userlist))