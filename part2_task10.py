word = int(input("write your number: "))
def fact(n):
    if n == 0:
        return 0
    else:
        return n + fact(n-1)
print(fact(word))