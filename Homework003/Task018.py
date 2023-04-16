#Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
#Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
#В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
#*Пример:*
#5
#1 2 3 4 5
#6
#-> 5
import random
numbers = []
length = int(input())
for i in range(length):
    numbers.append(random.randint(1, 100))
print(*numbers)
search = int(input())

#Function
def closest(numbers, search):     
    return numbers[min(range(len(numbers)), key = lambda i: abs(numbers[i]-search))]     
print(closest(numbers, search))