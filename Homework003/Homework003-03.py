# 3 - Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
# *Пример:*
# - [1.1, 1.2, 3.1, 5.567, 10.003] => 0.564 или 564

# Создание списка одним из следующих способов:
# 1 Спсоб
import random as rd
size = int(input('Выберите количество элементов списка: '))
userlist = list(rd.uniform(0, 20) for i in range(size))
print(userlist)

# 2 Спсоб
userlist2 = list(map(float, input('Задайте список чисел (десятичных дробей, желательно, через пробел): ').split()))
print(userlist2)

def dif_frac_parts(a: list):
    ''' программа ищет разницу между максимальным и минимальным значением дробной части элементов'''

    fpmax = fpmin = a[0] % 1
    for i in range(len(a)):
        if a[i] % 1 > a[0] % 1:
            fpmax = a[i] % 1
        elif a[i] % 1 < a[0] % 1:
            fpmin = a[i] % 1
    print('min= ', fpmin)
    print('max= ', fpmax)

    res = fpmax - fpmin
    return res

print('difference between fractional parts is: ', dif_frac_parts(userlist2))

