attack_power = int(input())
speed = int(input())
agility = int(input())

x = 50
result = attack_power * 4 + speed * 3 + agility * 2

print("Боеспособность персонажа:", result)
if result > x:
    print("Вам достался очень сильный персонаж!")
