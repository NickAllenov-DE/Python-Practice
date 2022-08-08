# 2- Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной
#     последовательности. Посмотрели, что такое множество? Вот здесь его не используйте.

import random as rd
n = int(input('Input amount of elements in start list: '))
start_list = [rd.randint(0, 99) for i in range(n)]
print('start_list: ', start_list)

def non_rep_list(a: list):
    new_list = []
    for i in range(len(a) - 1):
        if a[i] not in new_list:
            new_list.append(a[i])
    return new_list

print('List of non-repeated elements: ', non_rep_list(start_list))