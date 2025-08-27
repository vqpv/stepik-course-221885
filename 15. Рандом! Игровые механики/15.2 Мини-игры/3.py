import random


n = int(input())

armor_price = 100

a = 10
b = 20
discount = random.randint(a, b)

print("Вы покупаете доспехов:", n)
print("Скидка на каждый доспех:", discount)
print("Итоговая стоимость одного доспеха:", armor_price - discount)
print("Итоговая стоимость всей покупки:", (armor_price - discount) * n)
