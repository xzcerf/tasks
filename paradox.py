import random
a = random.randrange(0, 2)
b = random.randrange(0, 2)
c = random.randrange(0, 2)
while a == 0 and b == 0 and c == 0:
    a = random.randrange(0, 2)
    b = random.randrange(0, 2)
    c = random.randrange(0, 2)
    if a == 1 or b == 1 or c == 1:
        break
if a == 1:
    b = 0
    c = 0
elif c == 1:
    a = 0
    b = 0
elif b == 1:
    a = 0
    c = 0

d = str(input())
if d == 'a':
    if b == 0:
        print('b пустая')
    elif c == 0:
        print('c пустая')
if d == 'b':
    if a == 0:
        print('a пустая')
    elif c == 0:
        print('c пустая')
if d == 'c':
    if a == 0:
        print('a пустая')
    elif b == 0:
        print('b пустая')
        


