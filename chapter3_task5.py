l = [0,1,2,3,4,5,6,7,9]

for i in range(l.__len__()):
    if l[0] == 1:
        if i == l[i] - 1:
            continue
        else:
            print(i + 1)
            break
    elif l[0] < 0:
        print(1)
        break
    else:
        if i == l[i]:
            continue
        else:
            print(i)
            break