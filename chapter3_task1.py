text = input("your words: ")
def num_low(string):
    uppers = 0
    lowers = 0
    for x in string:
        if x.islower():
            lowers += 1
        elif x.isupper():
            uppers += 1
    print(f"Колличество букв в верхнем регистре {uppers}")
    print(f"Колличество букв в нижнем регистре {lowers}")   
num_low(text)
    