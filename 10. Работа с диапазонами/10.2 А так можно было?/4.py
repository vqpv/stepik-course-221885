s_1 = int(input())
s_2 = int(input())
s_3 = int(input())
s_4 = int(input())

s = (s_1 + s_2 + s_3 + s_4) / 4

a = 3000
b = 6000
c = 10000

if s < a:
    print("Пассивно...")
elif s < b:
    print("Нормальная активность")
elif s < c:
    print("Хорошая активность!")
else:
    print("Офигенская активность!")
