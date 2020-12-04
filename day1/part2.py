l = [int (i) for i in open ('input').readlines()]
for i in range(len(l)):
    for y in range(len(l)):
        for x in range(len(l)):
            if l[i] + l[x] + l[y] == 2020:
                print(l[i], l[x], l[y])
                print(l[i] * l[x] * l[y])
