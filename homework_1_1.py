# 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, 
# является ли этот день выходным.
# *Пример:*
# - 6 -> да
# - 7 -> да
# - 1 -> нет

# number = int(input('Введите номер дня недели: '))
# if number >= 1 and number < 6:
#     print('этот день недели НЕ является выходным')
# elif number > 6 and number < 8:
#     print('выходной!')
# else:
#     print('таких дней в неделе нет')

number = int(input('Введите номер дня недели: '))
if 0 < number < 6:
    print('этот день недели НЕ является выходным')
elif 6 < number < 8:
    print('выходной!')
else:
    print('таких дней в неделе нет')