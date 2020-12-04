def countTrees(stepX, stepY):
    tot = 0
    x = 0
    with open('input') as f:
        for y, l in enumerate(f):
            if stepY == 2 and y % 2 == 1:
                continue
            pos = l[x]
            if l[x] == '#':
                tot += 1
            x = (x + stepX) % len(l.rstrip())
    return tot


tot = countTrees(1, 1)
tot *= countTrees(3, 1)
tot *= countTrees(5, 1)
tot *= countTrees(7, 1)
tot *= countTrees(1, 2)

print(tot)
