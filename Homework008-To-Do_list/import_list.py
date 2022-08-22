
def import_tdlist():
    with open('To-Do_List.json', 'r', encoding='utf-8') as data:
        tdlist = json.load(data)

    return tdlist