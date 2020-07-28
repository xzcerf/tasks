wins = 0
loses = 0

def mh():
    import random
    global wins
    global loses

    door1 = door2 = door3 = 0


# получаем случайное число от 1 до 3, дверь, за которой приз
    random_value = random.randrange(1, 4)
    if random_value == 1:
        door1 = 1
    elif random_value == 2:
        door2 = 1
    elif random_value == 3:
        door3 = 1


# случайным образом выбирается одна дверь
    while True:
        user_value = random.randrange(1, 4)
        if user_value == 1:
            door1 = door1 + 2
        elif user_value == 2:
            door2 += 2
        elif user_value == 3:
            door3 += 2
        break


# получаем случайное число, чтобы открыть случайную пустую дверь
    while True:
        empty_door = random.randrange(1, 4)
        if empty_door == 1 and door1 == 0:
            door1 = -1
        elif empty_door == 2 and door2 == 0:
            door2 = -1
        elif empty_door == 3 and door3 == 0:
            door3 = -1
        else:
            continue
        break


    #меняем выбор
    while True:
        final_choice = 0
        if door1 != -1 and door1 < 2:
            door1 += 2
            final_choice = 1
        elif door2 != -1 and door2 < 2:
            door2 += 2
            final_choice = 2
        elif door3 != -1 and door3 < 2:
            door3 += 2
            final_choice = 3
        break

    if final_choice == random_value:
        wins += 1
    else:
        loses += 1


total_rounds = range(100)


for i in total_rounds:
    mh()


print(f'Победы: {wins}\nПоражения: {loses}')