#Последовательностью Фибоначчи называется последовательность чисел a0, a1, ..., an, ..., где
#a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
#Требуется найти N-е число Фибоначчи
#Input: 7
#Output: 21
#Задание необходимо решать через рекурсию

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0

#Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
#Input: 5 -> 1 3 3 3 4
#Output: 1 3 3 3 1

def change_rating(input_list):
    maxx = max(input_list)
    minn = min(input_list)

    for i in range(len(input_list)):
        if input_list[i] == maxx:
            input_list[i] = minn

    return input_list