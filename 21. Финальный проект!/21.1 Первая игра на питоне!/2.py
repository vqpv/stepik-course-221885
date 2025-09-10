import random


for _ in range(3):
    x = int(input())
    
    n = random.randint(1, 3)
    
    if x == n:
        print("Вау, вы настоящий волшебник!")
    else:
        print("Увы, в этот раз не повезло!")
