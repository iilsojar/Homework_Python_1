# 3. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся 
# элементов исходной последовательности в том же порядке.
# in
# 7
# out
# [4, 5, 3, 3, 4, 1, 2]
# [5, 1, 2]
# in
# -1
# out
# Negative value of the number of numbers!
# []
# in
# 10
# out
# [4, 4, 5, 5, 6, 2, 3, 0, 9, 4]
# [6, 2, 3, 0, 9]

lst = [int(s) for s in input('Задайте последовательность чисел: \n').split()]
print(f'исходный список => {lst}')
for i in range(len(lst)):
    for j in range(len(lst)):
        if i != j and lst[i] == lst[j]:
            break
    else: 
        print(lst[i], end = ' ')
print('<= список неповторяющихся элементов')



