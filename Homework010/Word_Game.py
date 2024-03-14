import random

hidden_word = []
gotten_word = []

list_of_word_simple = ['дом', 'дно', 'день', 'ночь', 'мир']
list_of_word_medium = ['дверь', 'шапка', 'кровать']
list_of_word_hard = ['параллелипипед', 'синхрофазатрон', 'циклопентанпергидрофенантрен', 'двадцатичетырехбуквенное']


def choosing_difficulty_level():
    level = input('Выберите уровень сложности:\n'
          '1 - Простой\n'
          '2 - Средний\n'
          '3 - Сложный   ')
    while level not in '123':
        level = input('Введено некорретное значение! Выберите 1, 2 или 3 ')
        continue

    if level == 1:
        return list_of_word_simple
    elif level == 2:
        return list_of_word_medium
    else:
        return list_of_word_hard


def choose_a_word(lst):
    global hidden_word
    hidden_word = random.choice(lst)
    print(hidden_word)
    print('Загадано слово - ', 'x' * len(hidden_word))
    return hidden_word


def checking_for_compliance(gotten_word, hidden_word):
    pass


def check_the_word(gotten_word, hidden_word):
    bull = 0
    cow = 0
    for k in gotten_word:
        if k in hidden_word:
            cow += 1
    for i in range(len(hidden_word)):
        if hidden_word[i] == gotten_word[i]:
            bull += 1
    res = ['Bulls - ', bull, 'Cows - ', cow - bull]
    print(res)

def game():
    choose_a_word(choosing_difficulty_level())
    steps = 0
    if checking_for_compliance(gotten_number=gotten_word, hidden_number=hidden_word):
        steps += 1
        if gotten_word == hidden_word:
            print('Поздравляем!!! Вы отгадали задуманное слово!')
            print('Вам понадобилось', steps, 'хода(ов)')
        else:
            check_the_word(gotten_number=gotten_word, hidden_number=hidden_word)
            print('Попробуйте еще раз :-)')

game()