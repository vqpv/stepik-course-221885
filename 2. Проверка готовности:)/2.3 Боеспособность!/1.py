name = input()
attack_power = int(input())
speed = int(input())
agility = int(input())
level = int(input())

result = (attack_power * 4 + speed * 3 + agility * 2) * level

print("Имя персонажа:", name)
print("Боеспособность персонажа:", result)
