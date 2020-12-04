keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # , 'cid'

tot = 0
x = 0
with open('input') as f:
    for l in f:
        d = {x.split(':')[0]: x.split(':')[1] for x in l.split()}
        for key in keys:
            if key not in d:
                break
            val = d[key]
            if key == 'byr':
                val = int(val)
                if val < 1920 or val > 2002:
                    break
            if key == 'iyr':
                val = int(val)
                if val < 2010 or val > 2020:
                    break
            if key == 'eyr':
                val = int(val)
                if val < 2020 or val > 2030:
                    break
            if key == 'hgt':
                cmin = val[-2:]
                if cmin not in ['cm', 'in']:
                    break
                val = int(val[:-2])
                if cmin == 'cm' and (val < 150 or val > 193):
                    break
                if cmin == 'in' and (val < 59 or val > 76):
                    break
            if key == 'hcl':
                if val[0] != '#' or len(val) != 7:
                    break
                try:
                    int(val[1:], 16)
                except:
                    break
            if key == 'ecl':
                if val not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
                    break
            if key == 'pid':
                if len(val) != 9:
                    break
                try:
                    int(val)
                except:
                    break
        else:
            tot += 1


print(tot)
