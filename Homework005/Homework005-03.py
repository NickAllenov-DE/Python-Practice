# 3-Создайте два списка — один с названиями языков программирования, другой — с числами от 1 до длины первого.
# ['python', 'c#']
# [1,2]
# Вам нужно сделать две функции: первая из которых создаст список кортежей, состоящих из номера и языка,
# написанного большими буквами.
# [(1,'PYTHON'), (2,'C#')]
# Вторая — которая отфильтрует этот список следующим образом: если сумма очков слова имеет в делителях номер, с которым
# она в паре в кортеже, то кортеж остается, его номер заменяется на сумму очков.
# [сумма очков c# = 102, в делителях есть 2 с которым в паре. Значит список будет]
# [(1,'PYTHON'), (102,'C#')]
# Если нет — удаляется. Суммой очков называется сложение порядковых номеров букв в слове. Порядковые номера смотрите
# в этой таблице, в третьем столбце: https://www.charset.org/utf-8
# Это — 16-ричная система, поищите, как правильнее и быстрее получать эти символы.
# Cложите получившиеся числа и верните из функции в качестве ответа вместе с преобразованным списком

from functools import reduce

with open('programm_languages.txt', 'r', encoding='utf-8') as file:
    languages = file.read().split('\n')
list_of_nums = [i for i in range(1, len(languages) + 1)]

def creare_list_of_tuples(lst1, lst2):
    return list(zip(lst1, [word.upper() for word in lst2]))

# print(creare_list_of_tuples(list_of_nums, languages))

def filter(list_of_tuples):
    final_list = []
    total = 0
    for number, language in list_of_tuples:
        points = reduce(lambda x, y: x + y, [ord(char) for char in language])
        if points % number == 0:
            total += points
            final_list.append((points, language))
    del list_of_tuples
    return total, final_list

print(filter(creare_list_of_tuples(list_of_nums, languages)))