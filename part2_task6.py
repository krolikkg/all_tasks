num = int(input("write your number: "))
num = abs(num)
count = 1
num //= 10
while num > 0:
    num //=10
    count+=1
print(count)
