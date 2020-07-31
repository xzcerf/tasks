from random import randrange

match = 0
not_match = 0


def birthday():
    global match
    global not_match
    d = {

    }

    for i in range(1, 24):
        k = f's{i}'
        d[k] = randrange(1, 365)

    n = 2
    a = 0

    while True:
        if n == 24:
            n = 1
            a += 1
        elif 1 + a == 24:
            #print('Дни рождения не совпали.')
            not_match += 1
            break
        elif 1 + a == n:
            n += 1
            continue
        elif d[f's{1 + a}'] == d[f's{n}']:
            match += 1
            #print(f'd[s{1 + a}] == d[s{n}]')
            #print('Дни рождения совпали!')
            break
        elif d[f's{1 + a}'] != d[f's{n}']:
            n += 1
            continue


for i in range(100):
    birthday()

print(f'Совпали: {match} раз\nНе совпали: {not_match} раз')


