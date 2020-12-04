l = [int (i) for i in open ('input').readlines()]
for i in range(len(l)):
    for y in range(i, len(l)):
        if l[i] + l[y] == 2020:
            print(l[i] * l[y])
