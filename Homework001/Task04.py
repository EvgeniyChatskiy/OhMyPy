# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#*Пример:*
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

overallCraneNum=int(input('Overall number of cranes (must be a number divisible by 6): '))
petyaCrane=int(overallCraneNum/6)
serejaCrane=petyaCrane
katyaCrane=(petyaCrane+serejaCrane)*2
print(f"Petya's cranes: {petyaCrane};",f"Sereja's cranes: {serejaCrane};", f"Katya's cranes: {katyaCrane}.")