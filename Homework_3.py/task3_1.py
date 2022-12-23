# 1. Задайте список, состоящий из произвольных чисел, количество 
# задаёт пользователь.
# Напишите программу, которая найдёт сумму элементов списка, 
# стоящих на нечётных позициях(не индексах).
# in
# 5
# out
# [10, 2, 3, 8, 9]
# 22

from random import sample

def lst (len_list):
    new_list = sample (range (1, len_list * 2), k = len_list)
    print(new_list)
    summ = 0
    for i in range(0, len(new_list), 2):
        summ = summ + new_list[i]
    print (f'сумма элементов на нечётных позициях: {summ}')

lst(int(input('Введите количество чисел: ')))



