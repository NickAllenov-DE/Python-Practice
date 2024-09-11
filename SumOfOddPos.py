# 1 - Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# *Пример:*
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint as rdi
newlist = [rdi(1, 50) for i in range(7)]
print(newlist)

def sum_of_odd(a: list):
    sum = 0
    for i in range(len(a)):
        if i % 2:           # Здесь я немного запутался: почему i % 2 то же самое что и i % 2 != 0 ?
            print(a[i])
            sum += a[i]
    return sum

print('сумма нечетных элементов = ', sum_of_odd(newlist))
