tot = 0
x = 0
with open('input') as f:
    for l in f:
        pos = l[x]
        if l[x] == '#':
            tot += 1
        x = (x + 3) % len(l.rstrip())
print(tot)
