#Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
#Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
#Выведите минимальное количество монет, которые нужно перевернуть

coins = int(input("Enter amount of coins: "))
turn_head = 0
turn_tail = 0
for i in range(coins):
    import random
    side = random.randint(1, 2)
    if side == 1:
        print(f'{i + 1} coin is "head"')
        turn_head += 1
    else:
        print(f'{i + 1} coin is "tail"')
        turn_tail += 1
if turn_head == coins or turn_tail == coins:
    print(f"Amount of coins to turn over is zero")
elif turn_head > turn_tail:
    print(f"Amount of coins to turn over: {coins - turn_head}")
elif turn_head == turn_tail:
    print(f"Amount of coins to turn over: {coins // 2}")
else:
    print(f"Amount of coins to turn over: {coins - turn_tail}")

    