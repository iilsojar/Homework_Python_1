# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# in
# 4
# out
# [2, 5, 8, 10]
# [20, 40]
# in
# 5
# out
# [2, 2, 4, 8, 8]
# [16, 16, 4]

from random import randint


number = int(input('Введите количество чисел: '))
lst1 = []
lst2 = []

for i in range(number):
    lst1.append(randint(1, 9))

for i in range(len(lst1)):
    while i < len(lst1)/2 + 1 and number > len(lst1)/2:
        number = number - 1
        a = lst1[i] * lst1[number]
        lst2.append(a)
        i += 1

print(lst1)
print(lst2)