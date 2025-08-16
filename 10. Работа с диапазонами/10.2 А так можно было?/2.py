h = int(input())

h_1 = 0
h_2 = 6
h_3 = 12
h_4 = 18
h_5 = 22
h_6 = 23

if h_1 < h < h_2 or h_5 < h <= h_6:
    print("ночь")
elif h < h_3:
    print("утро")
elif h < h_4:
    print("день")
elif h < h_5:
    print("вечер")
