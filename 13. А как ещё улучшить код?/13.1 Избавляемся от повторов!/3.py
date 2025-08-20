new_goods = 'не подключена'
new_sales = 'не подключена'

a = input()
b = input()

if a == "да":
    new_goods = "хочу"

if b == "да":
    new_sales = "хочу"

print("Рассылка о новых товарах:", new_goods)
print("Рассылка о новых скидках:", new_sales)
