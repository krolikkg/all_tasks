numbers = input("your nums: ")
steps = int(input("write step: "))
split_numbers = numbers.split()

if steps < 0:
    for num in range(steps):
        split_numbers.insert(0, split_numbers.pop())
    
        
    print(" ".join(split_numbers))
else:
    steps = abs(steps)
    for num in range(steps):
        split_numbers.append(split_numbers.pop(0))
   
        
    print(" ".join(split_numbers))
print(type(split_numbers))