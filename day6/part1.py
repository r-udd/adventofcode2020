tot = 0
s = set()
with open('input') as f:
    for l in f:
        if l == '\n':
            tot += len(s)
            s = set()
        else:
            s = s.union(set(l.rstrip()))
    tot += len(s)
print(tot)
