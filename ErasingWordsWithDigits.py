# 4- В текстовом файле удалить все слова, которые содержат хотя бы одну цифру.
# В файле содержится, например:
# Мама сшила м0не штаны и7з бере9зовой кор45ы 893. -> Мама сшила штаны.
#
# https://zen.yandex.ru/suite/a6424a0f-4fdb-44a1-95a0-9945e6f0a699
# Это на случай возникновения непонятных символов в файле.

text = 'Мама сшила м0не штаны и7з бере9зовой кор45ы 893'

# text2 = 'Однажды 2/12 позвали 3/13' \
#         '– Пойдемте, 3/13, пройдемся вечерком.' \
#         '– Ах, что Вы, 2/12, – смутились 3/13, ' \
#         '–Увидят 5/15, что Вы со мной вдвоём.' \
#         '– Пусть видят 5/15, – сказали 2/12, ' \
#         '–Мне это, 3/13, поверьте, все равно.' \
#         'Пусть знают 5/15, – сказали 2/12, ' \
#         '–Что я Вас, 3/13, люблю уже давно.' \
#         '– И я Вас, 2/12, – сказали 3/13, ' \
#         '–Пройдемте, 2/12, подайте мне пальто.' \
#         'Ну что нам 5/15, ну что нам 6/16,' \
#         'Ну что нам 7/17 и даже если 100!'

def erasing_words_with_digits(text):
    with open('text_with_digits.txt', 'w', encoding='utf-8') as data:
        data.write(text)

    path = 'text_with_digits.txt'
    data = open(path, 'r', encoding='utf-8')
    text = data.read()
    list_of_words = text.split()
    data.close()

    new_list = []
    for word in range(len(list_of_words)):
        if list_of_words[word].isalpha():
            new_list.append(list_of_words[word])
    new_text = " ".join(new_list)

    with open(path, 'w', encoding='utf-8') as data2:
        data2.write(new_text)

erasing_words_with_digits(text)
