biggest = 0
with open('input') as f:
    for l in f:
        n = l.replace('F', '0').replace(
            'B', '1').replace('R', '1').replace('L', '0')
        i = int(n, 2)
        if i > biggest:
            biggest = i
print(biggest)
