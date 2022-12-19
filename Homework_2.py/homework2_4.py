# Напишите программу, которая принимает на вход 2 числа.
# Получите значение N, для пустого списка, заполните числами в диапзоне [-N, N].
# Найдите произведение элементов на указанных позициях(не индексах).
# Enter the value of N: 5
# Position one: 1
# Position two: 2
# -> [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
# -> 20
# Enter the value of N: 4
# Position one: 20
# Position two: 22
# -> [-4, -3, -2, -1, 0, 1, 2, 3, 4]
# -> There are no values for these indexes!

num = int(input('Введите число N: '))
N = []
for i in range(-num, num + 1):
    N.append(i)
print(N)

pos_one = int(input('Введите позицию числа 1: '))
pos_two = int(input('Введите позицию числа 2: '))

result = N[pos_one - 1] * N[pos_two - 1]
print(result)

