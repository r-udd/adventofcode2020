def calc(exp):
    if len(exp) == 1:
        return int(exp[0])
    val1 = exp.pop()
    oper = exp.pop()
    val2 = exp.pop()
    if oper == '+':
        return calc(exp + [int(val1) + int(val2)])
    elif oper == '*':
        return calc(exp + [int(val1) * int(val2)])
    else:
        print('ERROR')

with open('test1') as f:
    for l in f:
        exp = l.split()
        exp.reverse()
        print(calc(exp))
