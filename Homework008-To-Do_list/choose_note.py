import json



def find_by_key(lst, key, value):
    return (dict_ for index, dict_ in enumerate(lst) if key in dict_ and dict_[key] == value)

def choosing_note():
    print('Выберите параметр для поиска записи:\n'
          '1 - Name\n'
          '2 - Description\n'
          '3 - Creation_date\n'
          '4 - Deadline\n'
          '5 - Status\n')

    num = input('Выберите действие: ')
    while num not in '12345':
        num = input('Введено некорректное значение, выберите параметр из списка: ')
        continue

    if num == 1:
        key = 'Name'
    elif num == 2:
        key = 'Description'
    elif num == 3:
        key = 'Creation_date'
    elif num == 4:
        key = 'Deadline'
    else:
        key = 'Status'

    value = input('Введите значение: ')

    with open('To-Do_List.json', 'r', encoding='utf-8') as tdlst:
        lst = json.load(tdlst)

    find_by_key(lst, key, value)


