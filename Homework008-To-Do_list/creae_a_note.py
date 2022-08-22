import json

def create_todolist():
    tdlist = [
        {
            'Name': 'Start',
            'Description': 'Make To-Do List programm',
            'Creation_date': '2022-08-22',
            'Deadline': '2022-08-22.20:00',
            'Status': 'in progress'
        }
    ]

    with open('To-Do_List.json', 'w', encoding='utf-8') as tdlst:
        json.dump(tdlist, tdlst)

create_todolist()