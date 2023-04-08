#Задача 2: Найдите сумму цифр трехзначного числа.
#*Пример:*
#123 -> 6 (1 + 2 + 3)
#100 -> 1 (1 + 0 + 0)

number = int(input('Please enter a three digit number:' ))
numSum = (number%10) + ((number//10)%10) + (number//100)
print("The number's sum is: ", numSum)