import random


armor_price = 500

a = 10
b = 150
discount = random.randint(a, b)

print("Размер вашей скидки:", discount)
print("Итоговая стоимость доспеха:", armor_price - discount)
