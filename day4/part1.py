keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # , 'cid'

tot = 0
x = 0
with open('input') as f:
    for l in f:
        d = {x.split(':')[0]: x.split(':')[1] for x in l.split()}
        for key in keys:
            if key not in d:
                break
        else:
            tot += 1


print(tot)
