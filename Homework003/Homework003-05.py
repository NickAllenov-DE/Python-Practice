# 5 - Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# *Пример:*
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи](https://clck.ru/sH87m)

usernum = int(input('Выберит количество элементов: '))

def fib(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    return fib(n - 1) + fib(n - 2)

def negafib(n):

    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return -1

    return negafib(n - 2) - negafib(n - 1)



def fib_plus_nega(n):
    ''' Программа выдает совмещенный ряд Фибоначчи и Негафибоначчи'''

    poslist = [0]
    neglist = []

    for i in range(1, usernum+1):
        poslist.append(fib(i))
    print(f"poslist - {poslist}")

    for i in range(1, usernum + 1):
        neglist.append(negafib(i))
    print(f"neglist - {neglist}")
    neglist.reverse()
    result = neglist + poslist

    return f"Combined list - {result}"

print(fib_plus_nega(usernum))