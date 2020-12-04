tot = 0
with open('input') as f:
    for l in f:
        siffror, bokstav, passw = l.split()
        minst,mest = map(lambda x: int(x)-1, siffror.split('-'))
        bokstav = bokstav[0]
        antal = passw.count(bokstav)
        #print(minst, mest, bokstav, passw, passw.count(bokstav))
        first = passw[minst]
        if bool(passw[minst] == bokstav) != bool(passw[mest] == bokstav):
            tot += 1

        #program = [int(x) for x in f.readline().split(',')]
print(tot)
