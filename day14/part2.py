import operator
import functools
mem = {}
with open('input') as f:
    for l in f:
        line = l.rstrip().split(' = ')
        if line[0].startswith('mask'):
            xlist = [i for i, c in enumerate(line[1]) if c == 'X']
            #andmask = functools.reduce(operator.add, ['1' if x == 'X' else x for x in line[1]])
            #andmaskint = int(andmask,2)
            ormask = functools.reduce(operator.add, ['0' if x == 'X' else x for x in line[1]])
            ormaskint = int(ormask,2)
        else:
            address = int(line[0].split('[')[1][:-1])
            value = int(line[1])

            #print('ad', format(address, '036b'))
            #print('| ', format(ormaskint, '036b'))
            #print('& ', format(andmaskint, '036b'))
            #print('a|', format(address | ormaskint, '036b'))
            straddr = format(address | ormaskint, '036b')
            for i in range(2**len(xlist)):
                xstring = format(i, '0' + str(len(xlist)) + 'b')
                #print(xstring)
                for y, xpos in enumerate(xlist):
                    #l = len(straddr)
                    #a = straddr[:xpos]
                    #b = xstring[y]
                    #c = straddr[xpos+1:]
                    straddr = straddr[:xpos] + xstring[y] + straddr[xpos+1:]
                mem[straddr] = value
                #print(f'addr: {int(straddr, 2)}, value: {value}')
            #print(index, format(value, '036b'))
            #print(index, format(mem[index], '036b'))
        #print(mem)
        #print()
#print(mem)
print(sum(mem.values()))
