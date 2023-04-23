#Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.
#*Пример:*
#A = 3; B = 5 -> 243 (3⁵)
#A = 2; B = 3 -> 8 

a = int(input())
b = int(input())
res = 1                    
def function(a, b, res):
    if b != 0:        
        res *= a
        function(a, b - 1, res)
    else:
        print(res)

function(a, b, res)
