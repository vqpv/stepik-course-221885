h = int(input())

h_1 = 6
h_2 = 12
h_3 = 18
h_4 = 22
h_5 = 24

if h in range(h_1) or h in range(h_4, h_5):
    print("ночь")
elif h in range(h_1, h_2):
    print("утро")
elif h in range(h_2, h_3):
    print("день")
elif h in range(h_3, h_4):
    print("вечер")
else:
    print("Ошибка, введите время в часах 0-23.")
