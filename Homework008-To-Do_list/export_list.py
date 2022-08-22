
def export(data):
    with open('To-Do_List.json', 'w', encoding='utf-8') as tdlst:
        json.dump(data, tdlst)