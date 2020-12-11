grid = [list(x) for x in open('input.txt').read().split('\n')]

import copy

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
        c0 = c[0]
        c1 = c[1]
        if grid[x + c0][y + c1] == '.':
            while (0 <= x+c0+c[0] <= len(grid)-1) and (0 <= y+c1+c[1] <= len(grid[0])-1):
                if grid[x + c0][y + c1] == '.':
                    c0 += c[0]
                    c1 += c[1]
                elif grid[x + c0][y + c1] in ['L', '#']:
                    break
        if grid[x + c0][y + c1] == '#':
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
            if old[x][y] != '.':
                n = checkNeighbours(old, x, y)
                # print(x, y, '=', n)
                if n == 0:
                    new[x][y] = '#'
                elif n >= 5:  # 4 in part 1
                    new[x][y] = 'L'
    # printgrid(new)
    return new


old = copy.deepcopy(grid)
# printgrid(old)
new = generation(old)

while new != old:
    old = copy.deepcopy(new)
    new = generation(old)

occupied = 0
for x in new:
    occupied += x.count('#')
# print('solution to part 1:', occupied)

print('solution to part 2:', occupied)
