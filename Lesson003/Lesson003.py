##Дан список чисел. Определите, сколько в нем встречается различных чисел.
##Input: [1, 1, 2, 0, -1, 3, 4, 4]
##Output: 6
##Примечание: Пользователь может вводить значения списка или список задан изначально.

#import random
#length = int(input("Enter list's length: "))
#list = []
#for i in range(length):
#    list.append(random.randint(-9, 10))
#print(list)
#print(len(set(list)))

##Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
##Input: [1, 2, 3, 4, 5] k = 2
##Output: [4, 5, 1, 2, 3]

#my_list = [1, 2, 3, 4, 5]
#k = 1
#for i in range(k):
#my_list.insert(0, my_list.pop())
#print(my_list)

##Напишите программу для печати всех уникальных значений в словаре.
##Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}]
##start_dict = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"},
##{" V ": "S009"}, {" VIII ": "S007"}]

#result_set = set()

#for mini_dict in start_dict:
#result_set = result_set.union(set(mini_dict.values()))

#print(result_set)

##Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) 
##Input: [0, -1, 5, 2, 3]
##Output: 2
##Пояснение: (-1 < 5, 2 < 3)

#my_list = [0, -1, 5, 2, 3]
#count = 0

#for i in range(1, len(my_list)):
#if my_list[i] > my_list[i - 1]:
#count += 1

#print(count)