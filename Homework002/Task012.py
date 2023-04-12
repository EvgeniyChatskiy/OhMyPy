#Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. 
#Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. 
#Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import random
number1 = random.randint(1, 11)
number2 = random.randint(1, 11)
summ = number1 + number2
prod = number1 * number2
answer1 = 0
answer2 = 0
print("Katya is trying to guess Petya's riddled number")
print(f"Hints: summary = {summ}; product = {prod}")
while (answer1 != number1 and answer2 != number2) and (answer1 != number2 and answer2 != number1):
    answer1 = int(input("Enter first number: "))
    answer2 = int(input("Enter second number: "))
print("Well done, Katya!")

