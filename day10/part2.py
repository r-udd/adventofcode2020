ones = 0
threes = 1 # Last is always three
arrs = 1
with open('test1') as f:
    l = map(int, f.readlines())
l.sort()
l.append(l[-1] + 3)
optional = []
subs = []
for i in range(len(l)-2):
    diff = l[i+1] - l[i]
    if diff == 3:
        subs.append(l[i], l[i+1])
    if diff == 1:
        optional.append(l[i+1])
    elif diff == 3:
        threes += 1

print(2 ** len(optional))
