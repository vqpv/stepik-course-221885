import random


a = 100
b = 300
x = random.randint(a, b)
y = random.randint(a, b)

print("Игрок умеет прыгать на:", x)
print("Перед игроком образовалась яма на:", y)

if x >= y:
    print("Вы преодолели яму!")
else:
    print("Эй там, на дне ямы, тебе не повезло, начни уровень заново!")
