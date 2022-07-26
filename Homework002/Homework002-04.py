# 4 - Реализуйте выдачу случайного числа (или алгоритм перемешивания списка)
# не использовать random.randint и вообще библиотеку random
# Можете использовать xor, биты, библиотеку time (миллисекунды или наносекунды) - для задания случайности

# Самый простой способ:
#
# randnum = int(input('Введите случайное число: '))
# print(randnum)

# Ну или:

# import time
# print(time.time())
# # или
# print(int(time.time()))

# Получится случайное неповторяющее число, хотя..., не случайное
#
import time
def rand_num(min, max):
    ''' Выдает случайное число из диапазона от min до max '''

    rand = int((time.time() % 0.1) * int(time.time()))
    print('rand ', rand)
    if rand % 2 == 0:
        devi = (rand % 1000) / 1000
    else:
        devi = ((rand % 1000) * -1) / 1000
    print('devi ', devi)
    half = (max - min) / 2
    print('half ', half)
    mid = max - half
    print('mid ', mid)
    shift = half * devi
    print('shift ', shift)
    result = int(mid + shift)
    return result

min = int(input('Введите нижнюю (левую) границу диапазона: '))
max = int(input('Введите верхнюю (правую) границу диапазона: '))
print('Ваше случайное число: ', rand_num(min, max))

# Вроде, получилось что-то более-менее внятное и не сильно мудреное, даже работает как требуется.
# Но все равно сильно далеко от нормального ГПСЧ и, тем более от ГСЧ.
# Правда, без проверок (как и все остальные ДЗ); виноват, чуть отстал, не хватает времени.