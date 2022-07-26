# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# *Пример:*
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

def list_of_mult(n):
    ''' param n: целое положительное число, return: список последовательных произведений от 1 до n '''

    listofmult = []
    m = 1
    for i in range(1, n+1):
        m = m * i
        listofmult.append(m)

    return listofmult

usernum = int(input('Ввдеите целое положительное число: '))
print(list_of_mult(usernum))
