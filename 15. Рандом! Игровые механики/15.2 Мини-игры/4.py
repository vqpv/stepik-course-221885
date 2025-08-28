import random


armor_price = 100

discount = random.randint(1, 3) * 10

print("Размер вашей скидки:", discount)
print("Итоговая стоимость доспеха:", armor_price - discount)
