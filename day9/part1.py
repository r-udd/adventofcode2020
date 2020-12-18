import itertools
preamble = 25
with open('input') as f:
    l = map(int, f.readlines())
    for i in range (preamble, len(l)):
        combs = list(itertools.combinations(l[i-preamble:i], 2))
        temp = map(lambda x: x[0] + x[1] == l[i], combs)
        if not any(map(lambda x: x[0] + x[1] == l[i], combs)):
            print(l[i])
            break
