import random


n = int(input())

if n == 1:
    x = random.randint(-2, 10)
elif n == 2:
    x = random.randint(-10, 25)

print("Вы двигаетесь на:", x)
