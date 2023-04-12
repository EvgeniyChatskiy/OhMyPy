#Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Enter the number: "))
two = 1
while two < number:
    print(two)
    two *= 2
