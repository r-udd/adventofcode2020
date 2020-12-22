import itertools

def p(grid):
    for line in grid:
        for x in line:
            print(x, end='')
        print()
    print()

grid = []
with open('input') as f:
    grid = list(map(lambda x: list(x[:-1]), f.readlines()))


maxx = len(grid[0])
maxy = len(grid)
dirs = list(itertools.product([-1, 0, 1],[-1, 0, 1]))
dirs.remove((0,0 ))
changed = True
while changed:
    #p(grid)
    newgrid = [['.' for _ in range(maxx)] for _ in range(maxy)]
    changed = False
    for y in range(1, maxy - 1):
        for x in range(1, maxx - 1):
            count = 0
            if grid[y][x] == '.':
                continue
            for d in dirs:
                newx = x + d[0]
                newy = y + d[1]
                count += grid[newy][newx] == '#'
            if grid[y][x] == 'L' and count == 0:
                newgrid[y][x] = '#'
                changed = True
            elif grid[y][x] == '#' and count >= 4:
                newgrid[y][x] = 'L'
                changed = True
            else:
                newgrid[y][x] = grid[y][x]
    grid = newgrid

print(sum(map(lambda x: x.count('#'), grid)))
