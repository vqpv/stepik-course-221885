import random


n = int(input())

if n == 1:
    x = random.randint(-2, 10)
elif n == 2:
    x = random.randint(-10, 25)

if x <= 0:
    print("Увы, вам выпало:", x)
    print("Вы ничего не получаете")
else:
    print("Ура, вы получаете ходов:", x)
