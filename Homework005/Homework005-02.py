# 2- Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Тот, кто берет последнюю конфету - проиграл.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random
from termcolor import cprint, colored

_holder = 0

def put_candies():
    global _holder
    _holder = 2021

def game_mode():
    mode = 0
    while mode != 1 or mode != 2 or mode != 3:
        mode = int(input('Выберите режим игры: \n'
                         '1 - Игрок против игрока\n'
                         '2 - Игрок против комрьютера\n'
                         '3 - Игрок против "умного" бота   '))
        if mode < 1 or mode > 3:
            print('Введено некорректное значение! Выберите 1, 2, или 3')
            continue
        return mode

def bot():
    global _holder
    if _holder > 28:
        bot_takes = random.randint(1, 28)
    else:
        bot_takes = random.randint(1, _holder)
    print(f"Компьютер взял {bot_takes} конфет")
    _holder -= bot_takes
    return _holder

def advanced_bot():
    global _holder
    if _holder > 28:
        bot_takes = _holder % 29
        if bot_takes == 0:
            bot_takes = random.randint(1, 28)
    else:
        bot_takes = _holder - 1 if _holder != 1 else 1
    print(f"Компьютер взял {bot_takes} конфет")
    _holder -= bot_takes
    return _holder

def choosing_players(names: list, mode: int):
    count = True
    while count:
        if mode == 1:
            names[0] = input('Игрок 1, представьтесь, пожалуйста: ')
            names[1] = input('Игрок 2, представьтесь, пожалуйста: ')
            count = False
        elif mode == 2:
            names[0] = input('Игрок 1, представьтесь, пожалуйста: ')
            count = False
        else:
            names[0] = input('Игрок 1, представьтесь, пожалуйста: ')
            count = False
    return names

def toss(name1, name2):
    print('Жеребьевка. Сейчс мы определим кто будет брать конфеты первым с помощью имитации игральной кости')
    a = b = 7
    while a == b:
        print(f"Кубик бросает игрок {name1}")
        a = random.randint(1, 6)
        print(f"У {name1} выпало", a)
        print(f"Теперь очередь игрока {name2}")
        b = random.randint(1, 6)
        print(f"У {name2} выпало", b)
        if a > b:
            print('Первым ходит', name1)
            return name1
        elif a < b:
            print('Первым ходит', name2)
            return name2
        else:
            continue

def take_candies():
    global _holder
    switcher = True
    while switcher:
        amount = int(input(colored('Сколько конфет берем? ', color='magenta')))
        if amount <= 0 or amount > 28:
            cprint('Введено недопустимое значение! Вы можете взять от 1 до 28 конфет!', color='yellow')
            continue
        elif amount > _holder:
            cprint(f'Ошибка! На столе {_holder} конфет. Вы не можете взять больше {_holder} конфет', color='yellow')
            continue
        else:
            _holder -= amount
            switcher = False

def check_amount():
    global _holder
    return _holder

def is_gameover():
    global _holder
    return _holder == 0

def game():
    print('Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.\n '
          'Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.\n '
          'Тот, кто берет последнюю конфету - проиграл.')
    names = ['Nick Allenov', 'Nikolai Allenov']
    mode = game_mode()
    choosing_players(names, mode)
    user_name1 = names[0]
    user_name2 = names[1]
    turn = toss(user_name1, user_name2)
    cprint('Начало игры!', color='red', attrs=['bold', 'underline'])
    put_candies()
    while True:
        cprint(f"На столе конфет - {check_amount()}", color='green', attrs=['underline'])
        user_color = 'blue' if turn == user_name1 else 'cyan'
        cprint(f"Ход игрока {turn}", color=user_color)
        cprint('Вы можете взять от 1 до 28 конфет.', color=user_color)
        if turn == user_name1:
            take_candies()
        else:
            if mode == 2:
                bot()
            else:
                advanced_bot()
        turn = user_name2 if turn == user_name1 else user_name1
        if is_gameover():
            break
    print()
    cprint(f"Выиграл игрок {turn}. !!!Поздравляем!!!", color='cyan', attrs=['bold', 'underline', 'reverse'])

game()
