import random


x = int(input())
y = random.randint(1, 3)

if x == y:
    print("Удар заблокирован, бот вас переиграл и уничтожил!")
else:
    print("Вы пробили бота! Вы маэстро!")
