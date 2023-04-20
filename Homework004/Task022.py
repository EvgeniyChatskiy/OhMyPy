#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
#Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества. Затем пользователь вводит сами элементы множеств.

import random
n = int(input("Введите количество чисел первого набора: "))
m = int(input("Введите количество чисел второго набора: "))
list_one = []
list_two = []
new_list = []
for i in range(n):
    list_one.append(random.randint(1, 10))
for i in range(m):
    list_two.append(random.randint(1, 10))
for i in list_one:
    for j in list_two:
        if j in list_one:
            new_list.append(j)
new_list = list(dict.fromkeys(new_list))
new_list.sort()
print(f"первый набор чисел: ", list_one)
print(f"Второй набор чисел: ", list_two)
print(f"Пересекающиеся числа двух наборов: ", new_list)