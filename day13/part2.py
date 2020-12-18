with open('input') as f:
    _ = int(f.readline())
    l = [int(y) for y in f.readline().rstrip().split(',') if y != 'x']
    s = f.readline().rstrip().split(',')
    offsets = [x for x in l]
diff = map(lambda x: x - start % x, l)
print(start)
print(l)
print(diff)
m = min(diff)
i = diff.index(m)
print(m * l[i])
