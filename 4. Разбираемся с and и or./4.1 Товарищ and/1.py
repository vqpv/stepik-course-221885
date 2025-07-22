title = input()
genre = input()
rating = int(input())

if genre == "мелодрама" and rating > 7:
    print("Да, директор заценит!")
else:
    print("Не, это кино директору лучше не предлагать...")
