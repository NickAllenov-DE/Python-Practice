import show_all
import add_note
import edit_note
import delete_note
import change_ststus

def choose_operation():
    print('Вы находитесь в основном меню, ниже приведены возможные варианты действий:\n'
            '1 - Посмотреть список дел.\n'
            '2 - Добавить запись.\n'
            '3 - Редактировать запись.\n'
            '4 - Удалить запись.\n'
            '5 - Изменить статус записи.\n'
            '6 - Выход.\n')

    usernum = input('Выберите действие: ')
    actions = '123456'
    while usernum not in actions:
        usernum = input('Введено некорректное значение, выберите действие из списка: ')
        continue

    if usernum == 1:
        show_all.show_tdlist()
    elif usernum == 2:
        add_note.add_note()
    elif usernum == 3:
        edit_note.edit_note()
    elif usernum == 4:
        delete_note.delete_note()
    elif usernum == 5:
        change_ststus.change_note()
    else:
        print('Всего доброго) Возвращайтесь ещё.')
        exit()
