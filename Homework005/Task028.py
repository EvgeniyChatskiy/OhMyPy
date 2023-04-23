#Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
#Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.
#*Пример:*
#2 2
#4 

a = int(input())
b = int(input())
temp = 0
result = 0
def summ(a, b, result, temp):
    if result < a:
        result += 1
        summ(a, b, result, temp)
    elif temp < b:
        result += 1
        summ(a, b, result, temp + 1)
    else:
        print(result)

summ(a, b, result, temp) 