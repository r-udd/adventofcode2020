ones = 0
threes = 1 # Last is always three
curr = 0
with open('input') as f:
    l = map(int, f.readlines())
l.sort()

for i in l:
    diff = i - curr
    curr = i
    if diff == 1:
        ones += 1
    elif diff == 2:
        print('fail')
    elif diff == 3:
        threes += 1

print(ones * threes)
