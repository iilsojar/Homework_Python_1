# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Без использования встроенной функции преобразования, без строк.
# in
# 88
# out
# 1011000
# in
# 11
# out
# 1011

a = int(input('Введите десятичное число для преобразования в двоичное: '))
number = '' 
while a > 0:
    number = str(a % 2) + number
    a = a // 2
print (number)


