p1 = []
p2 = []
with open('input') as f:
    l = f.readlines()
    p1 = [int(x) for x in l[1:l.index('\n')]]
    p2 = [int(x) for x in l[l.index('Player 2:\n') + 1:]]

while len(p1) and len(p2):
    if p1[0] > p2[0]:
        p1.append(p1[0])
        p1.append(p2[0])
        p1.remove(p1[0])
        p2.remove(p2[0])
    elif p1[0] < p2[0]:
        p2.append(p2[0])
        p2.append(p1[0])
        p1.remove(p1[0])
        p2.remove(p2[0])
    else:
        print('Error')
if len(p1):
    winner = p1
else:
    winner = p2
print(sum([c * (len(winner) - i) for i, c in enumerate(winner)]))
