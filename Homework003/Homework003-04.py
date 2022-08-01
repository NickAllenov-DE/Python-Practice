# 4 - Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# *Пример:*
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

usernum = int(input('Введите чило в десятичной системе: '))

def dec_to_bin(usernum):
    ''' программа преобразовывает десятичное число в двоичное '''

    numbin = ''
    while usernum > 0:
        numbin = str(usernum % 2) + numbin
        usernum = usernum // 2

    return int(numbin)    # Можно без int, тогда получится строка, но визуально то же самое

print(dec_to_bin(usernum))