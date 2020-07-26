import random
door1 = door2 = door3 = False
random_value = random.randrange(1,4)
if random_value == 1:
    door1 = True
elif random_value == 2:
    door2 = True
elif random_value == 3:
    door3 = True

print('Выберите значение двери от единицы до тройки')
while True:
    answer = input()
    change = answer.replace('.', '', 1)
    if not change.isdigit():
        print('Нужно ввести число')
    elif change != answer:
        print('Нужно выбрать одну из трёх дверей')
    elif int(change) > 3 or int(change) < 1:
        print('На выбор есть только три двери')
    elif change == answer:
        answer = int(answer)
        break

if answer == 1:
    answer = door1
    if answer:
        random = random.randrange(2,4)
    if random == 2:
        print('Мы подскажем вам: за второй дверью пусто')
    elif random == 3:
        print('Мы подскажем вам: за третьей дверью пусто')
    if not answer:
        if door2:
            print('Мы подскажем вам: за третьей дверью пусто')
        elif door3:
            print('Мы подскажем вам: за второй дверью пусто')
if answer == 2:
    answer = door2
    if answer:
        random = random.randrange(1, 4, 2)
    if random == 1:
        print('Мы подскажем вам: за первой дверью пусто')
    elif random == 3:
        print('Мы подскажем вам: за третьей дверью пусто')
    if not answer:
        if door1:
            print('Мы подскажем вам: за первой дверью пусто')
        elif door3:
            print('Мы подскажем вам: за третьей дверью пусто')
if answer == 3:
    answer = door3
    if answer:
        random = random.randrange(1,3)
    if random == 1:
        print('Мы подскажем вам: за первой дверью пусто')
    elif random == 2:
        print('Мы подскажем вам: за второй дверью пусто')
    if not answer:
        if door1:
            print('Мы подскажем вам: за первой дверью пусто')
        elif door2:
            print('Мы подскажем вам: за второйдверью пусто')
