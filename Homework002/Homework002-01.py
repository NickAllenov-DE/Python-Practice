# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# *Пример:*
# - 6782 -> 23
# - 0,56 -> 11

# def sum_of_dig1(n):
#     ''' param n: вещественное число; return: сумма цифр в числе '''
#
#     res = 0
#
#     if snum[0] == '-':
#         modnum = float(snum) * (-1)
#     else:
#         modnum = float(snum)
#
#     inum = int(round((modnum * (10 ** (len(snum) - 2))), 1))
#
#     for i in range(int(len(str(inum)))):
#         res += int(str(inum)[i])
#     return res
#
# snum = str(input('Введите число (только рациональное, пожалуйста): '))
# print('Сумма цифр в числе равна: ', sum_of_dig1(snum))

# В данном варианте есть важное ограничение по использованию десятичных дробей - нельзя использовать запятую как
# разделитель, либо нужно принимать вводимое значение типом float и затем конвертировать в str.
# Но, в целом, вариант рабочий, несмотря на немного перегруженный код

def sum_of_dig2(n):
    ''' param n: вещественное число; return: сумма цифр в числе '''

    listofdig = []
    for i in usernum:
        if i.isdigit():
            listofdig.append(int(i))
    print(listofdig)

    # res = sum(listofdig)     # Так будет короче, но, если не использовать встроенные функции, то:

    res = 0
    for i in listofdig:
        res += i

    return res

usernum = input('Введите число: ')
print('Сумма цифр в числе равна: ', sum_of_dig2(usernum))

# Так получше будет :)
