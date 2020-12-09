seats = range(0, 1024)
with open('input') as f:
    for l in f:
        n = l.replace('F', '0').replace(
            'B', '1').replace('R', '1').replace('L', '0')
        i = int(n, 2)
        seats.remove(i)

for i, seat in enumerate(seats):
    if i == 0:
        continue
    if seats[i-1] != seat - 1:
        print(seat)
        break
