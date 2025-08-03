a = int(input())
b = input()
c = int(input())

if b == "+":
    print(a + c)
elif b == "-":
    print(a - c)
elif b == "*":
    print(a * c)
elif b == "/":
    print(a / c)
else:
    print("Не знаю такого действия...")
    print("Чтобы я посчитала, введите: + - * /")
