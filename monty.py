import random
a = 2 #дверь, за которой приз
n1 = random.randrange(1,4) #выбираем случайную дверь
if n1 == 2: #Если мы выбрали вторую, то нам показывают, что в 1-й или 3-й пусто и при смене выбора мы проигрываем
    n1 = 3
    print('Вы проиграли')
elif n1 == 1:#Если мы выбрали первую, то нам показывают, что в третьей пусто и при смене выбора мы выигрываем
    n1 = 2
    print('Вы победили')
elif n1 == 3: #Если мы выбрали третью, то нам показывают, что в первой пусто и при смене выбора мы выигрываем
    n1 = 2
    print('Вы победили')

