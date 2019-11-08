count = True
def superDigit(n, k = 1):
    n = str(n) * k
    p = 0

    for i in n:
        p += int(i)

    global count

    if count:
        if int(str(p).__len__()) < 2:
            count = False

        p = int(superDigit(p))
 
    return p
total = superDigit(9875, 4)
print(total)