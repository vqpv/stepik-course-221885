import random


random_number = random.randint(1, 8)

if random_number == 1:
    print("Заморозка времени")
elif random_number == 2:
    print("Невидимость")
elif random_number == 3:
    print("Чтение мыслей")
elif random_number == 4:
    print("Защитное поле")
else:
    print("Увы, ничего не выпало, повезёт в следующий раз!")
