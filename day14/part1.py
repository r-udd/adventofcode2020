import operator
import functools
mem = {}
with open('input') as f:
    for l in f:
        line = l.rstrip().split(' = ')
        if line[0].startswith('mask'):
            andmask = functools.reduce(operator.add, ['1' if x == 'X' else x for x in line[1]])
            andmaskint = int(andmask,2)
            ormask = functools.reduce(operator.add, ['0' if x == 'X' else x for x in line[1]])
            ormaskint = int(ormask,2)
        else:
            index = line[0].split('[')[1][:-1]
            value = int(line[1])
            mem[index] = value & andmaskint | ormaskint
            #print(index, format(value, '016b'))
            #print(index, format(mem[index], '016b'))
        #print(mem)
print(mem)
print(sum(mem.values()))
