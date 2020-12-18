import itertools
with open('input') as f:
    numbers = map(int, f.readlines())
    for l in range(2, len(numbers)):
        for i in range(len(numbers)):
            if sum(numbers[i:i+l]) == 776203571:
                print(min(numbers[i:i+l]) + max(numbers[i:i+l]))
