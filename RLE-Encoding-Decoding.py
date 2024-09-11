# 4- Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах

line1 = 'ddddjhhhjfjfjjjjrurrueieiiiiiwwwwhhhrrllllldddddddnnnnjjjjjuududduuudussisiiikaaaaaakkkkkyyyyyyeeeeegggggsfdgvc'
line2 = '2r3t4y5h6g7f4d3s1a7j8k'

with open('Uncompressed_data', 'w', encoding='utf-8') as data:
    data.write(line1)

with open('Uncompressed_data', 'r') as text:
    data1 = text.read()

def rle_encode(data):
    encoding = ''
    prev_char = ''
    count = 1
    if not data:
        return ''
    for char in data:
        if char != prev_char:
            if prev_char:
                encoding += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    else:
        encoding += str(count) + prev_char
    return encoding

print(rle_encode(data1))


with open('Compressed_data', 'w', encoding='utf-8') as data:
    data.write(line2)

with open('Compressed_data', 'r') as text2:
    data2 = text2.read()

def rle_decode(data):
    decode = ''
    count = ''
    for char in data:
        if char.isdigit():
            count += char
        else:
            decode += char * int(count)
            count = ''
    return decode

print(rle_decode(data2))
