def calc(exp):
    if len(exp) == 1:
        return int(exp[0])

    val1 = exp.pop()
    oper = exp.pop()
    val2 = exp.pop()
    if val1[0] == '(':
        calc(exp + [val2, oper, val1[1:]])
    elif val2[-1] == ')' and oper == '+':
        return int(val1) + int(val2)
    elif val2[-1] == ')' and oper == '*':
        return int(val1) * int(val2)
    elif oper == '+':
        return calc(exp + [str(int(val1) + int(val2))])
    elif oper == '*':
        return calc(exp + [str(int(val1) * int(val2))])
    else:
        print('ERROR')

with open('test2') as f:
    for l in f:
        exp = l.split()
        exp.reverse()
        print(calc(exp))
