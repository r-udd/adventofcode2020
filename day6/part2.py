tot = 0
yes = [0] * 26
counter = 0
with open('input') as f:
    for l in f:
        if l == '\n':
            tot += yes.count(counter)
            counter = 0
            yes = [0] * 26
        else:
            counter += 1
            s = set()
            s = s.union(set(l.rstrip()))
            for c in s:
                yes[ord(c) - ord('a')] += 1
    tot += yes.count(counter)
print(tot)
