import random


random_number = random.randint(1, 3)

if random_number == 1:
    print("Враг нападает на вас", "сверху")
elif random_number == 2:
    print("Враг нападает на вас", "слева")
elif random_number == 3:
    print("Враг нападает на вас", "справа")
