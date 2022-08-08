# 3- Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# Пример: при N = 12 -> [2, 3]

usernum = int(input('Input any natural number: '))
# def list_of_dividers(num):
#     listof = []
#     for i in range(2, 10):
#         if num % i == 0:
#             listof.append(i)
#     if len(listof) > 0:
#         conclusion = listof
#     else:
#         conclusion = "Your number doesn't have any factors"
#     return conclusion
# print(list_of_dividers(usernum))
#
# Тут немного не то получилось

def list_of_simple_factors(num):
    listosf = []
    i = 2
    while i <= num:
        while num % i == 0:
            listosf.append(i)
            num /= i
        i += 1
    if num > 1:
        listosf.append(num)
    print(listosf)
    set_of_fact = set(listosf)
    print(set_of_fact)
    new_list = list(set_of_fact)
    return new_list
print('Factors for your number is: ', list_of_simple_factors(usernum))
