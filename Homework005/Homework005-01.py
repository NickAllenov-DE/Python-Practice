# 1- Напишите программу, удаляющую из текста все слова, содержащие ""абв"".
# 'абвгдейка - это передача' = >" - это передача"

line1 = 'абвгдейка - это передача'
line2 = 'остались перекрестки строки и перенос слова переоборудование'
fragment1 = 'абв'
fragment2 = 'пере'

def fragment_eraser(line, fragment):
    print(line)
    words = line.split()
    new_words = []
    for word in words:
        if not fragment in word:
            new_words.append(word)
    new_line = ' '.join(new_words)
    return new_line
print(fragment_eraser(line2, fragment2))