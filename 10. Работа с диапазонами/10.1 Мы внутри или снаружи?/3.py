w = int(input())

a = 35
b = 50
c = 65

if w in range(a):
    print("Группа 1")
elif w in range(a, b):
    print("Группа 2")
elif w in range(b, c):
    print("Группа 3")
elif w > c:
    print("Группа 4")
