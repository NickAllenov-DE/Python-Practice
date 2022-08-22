import interface

def another_action():
    print('Желаете выполнить другое действие?')
    choice = input('\n 1 - Да, пожалуйста.\n 2 - Нет, спасибо.\n')

    while choice not in '12':
        choice = input('Простите, не понимаю. Выберите 1 или 2')
        continue

    if choice == 1:
        interface.choose_operation()
    else:
        print('Всего доброго) Возвращайтесь снова.')
        exit()