import copy

grid = open('inputs/input18.txt').read().split('\n')
grid = [list(x) for x in grid]

# a b c
# d o e
# f g h


def checkNeighbours(grid, x, y):
    neighbours = {'a': (-1, -1), 'b': (-1, 0), 'c': (-1, 1),
                  'd': (0, -1),                'e': (0, 1),
                  'f': (1, -1),  'g': (1, 0),  'h': (1, 1)}
    if x == 0:
        neighbours.pop('a', None)
        neighbours.pop('b', None)
        neighbours.pop('c', None)
    elif x == len(grid)-1:
        neighbours.pop('f', None)
        neighbours.pop('g', None)
        neighbours.pop('h', None)
    if y == 0:
        neighbours.pop('a', None)
        neighbours.pop('d', None)
        neighbours.pop('f', None)
    elif y == len(grid[0])-1:
        neighbours.pop('c', None)
        neighbours.pop('e', None)
        neighbours.pop('h', None)

    occupied = 0
    for n, c in neighbours.items():
        if grid[x + c[0]][y + c[1]] == '#':
            occupied += 1
    return occupied


def printgrid(grid):
    for x in grid:
        print(''.join(x))
    print('')


def generation(grid):
    old = copy.deepcopy(grid)
    new = copy.deepcopy(grid)
    for x in range(len(old)):
        for y in range(len(old[0])):
            n = checkNeighbours(old, x, y)
            if old[x][y] == '#':
                if n != 2 and n != 3:
                    new[x][y] = '.'
            elif old[x][y] == '.':
                if n == 3:
                    new[x][y] = '#'
    # printgrid(new)
    return new


old = copy.deepcopy(grid)
# printgrid(old)
new = generation(old)

i = 0
while i < 99:
    old = copy.deepcopy(new)
    new = generation(old)
    i += 1

on = 0
for x in new:
    on += x.count('#')

print('solution to part 1:', on)