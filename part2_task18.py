num = float(input("write your number: "))

i = 0

while i != num:
    if num % 2 != 0:
        i += 1
        a = i % 2 != 0
        print(a)
    else:
        i += 2
        print(i)
