﻿#Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками 
#(то есть разломить шоколадку на два прямоугольника).
#*Пример:*
#3 2 4 -> yes
#3 2 1 -> no

x = int(input("X = "))
y = int(input("Y = "))
k = int(input("Amount = "))
if (k % x == 0 or k % y == 0) and x * y != k:
    print("YES")
else:
    print("NO")                                