﻿#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, причём кусты высажены только по окружности. 
#Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
#Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — на i-ом кусте выросло ai ягод.
#В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. 
#Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
#Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.

import random
n = int(input("Введите количество кустов: "))
gryadka = []
max_num = 0
for i in range(n):
	gryadka.append(random.randint(1, 10))
print(gryadka)
for i in range(n):
	if i == 0:
		if (gryadka[0] + gryadka[-1] + gryadka[1]) > max_num:
			max_num = gryadka[0] + gryadka[-1] + gryadka[1]
	elif i == n - 1:
		if (gryadka[i - 1] + gryadka[-1] + gryadka[0]) > max_num:
			max_num = gryadka[i - 1] + gryadka[-1] + gryadka[0]
	else:
		if (gryadka[i] + gryadka[i - 1] + gryadka[i +1]) > max_num:
			max_num = gryadka[i] + gryadka[i - 1] + gryadka[i +1]
print(f"Максимальное количетво ягод с куста: ", max_num)