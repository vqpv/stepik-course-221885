import random


number_guesses = 0

for _ in range(3):
    x = int(input())
    
    n = random.randint(1, 3)
    
    if x == n:
        number_guesses += 1
        print("Вау, вы настоящий волшебник!")
    else:
        print("Увы, в этот раз не повезло!")

print("Количество отгадок:", number_guesses)
