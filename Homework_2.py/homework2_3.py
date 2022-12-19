# Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
# in 
# 6
# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
# 14.071

num_list = []
num = (int(input('введите число n: ')))
for i in range(1, num + 1):
    num_list.append((1 + 1 / i) ** i)
    newlist = [round(float(i), 3) for i in num_list]
print(newlist)

sum = 0
for i in newlist:
    sum += i

print(f'Сумма всех чисел последовательности = > {sum:.5}')
