#Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

length = int(input("Длина списка: "))
low = int(input("Минимальный порог: "))
high = int(input("Максимальный порог: "))
my_list = []
result_list = []

for i in range(length):
    my_list.append(random.randint(-99, 100))
    if (my_list[i] > low) and (my_list[i] < high):
       result_list.append(i) 
print("Сгенерированный список: ", my_list)
print("Индексы чисел, входящих в диапазон значений: ",result_list)