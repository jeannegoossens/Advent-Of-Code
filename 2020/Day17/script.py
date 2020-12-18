import copy

grid = open('inp.txt').read().split('\n')
# grid = [[list(x) for x in grid],
#         [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))],
#         [['.' for _ in range(len(grid[0]))] for _ in range(len(grid))]]
print(grid)

# a b c         i j k           r s t
# d . e         l m n           u v w
# f g h         o p q           x y z

g = {}

for line in range(len(grid)):
    for c in range(len(grid[0])):
        if grid[line][c] == '#':
            g[(line, c, 0)] = '#'
        else:
            g[(line, c, 0)] = '.'

def print_coos(g):
    for k in sorted(g.keys()):
        print(g[k])

print_coos(g)


def checkNeighbours(grid, x, y, z):
    neighbours = {'a': (-1, -1, 0), 'b': (-1, 0, 0), 'c': (-1, 1, 0),
                  'd': (0, -1, 0),                   'e': (0, 1, 0),
                  'f': (1, -1, 0),  'g': (1, 0, 0),  'h': (1, 1, 0),
                  'i': (-1, -1, -1), 'j': (-1, 0, -1), 'k': (-1, 1, -1),
                  'l': (0, -1, -1), 'm': (0, 0, -1), 'n': (0, 1, -1),
                  'o': (1, -1, -1), 'p': (1, 0, -1), 'q': (1, 1, -1),
                  'r': (-1, -1, 1), 's': (-1, 0, 1), 't': (-1, 1, 1),
                  'u': (0, -1, 1), 'v': (0, 0, 1), 'w': (0, 1, 1),
                  'x': (1, -1, 1), 'y': (1, 0, 1), 'z': (1, 1, 1)}

    occupied = 0
    for n, c in neighbours.items():
        try:
            if grid[x + c[0]][y + c[1]][z + c[2]] == '#':
                occupied += 1
        except IndexError:
            continue
    return occupied


def printgrid(grid):
    print('\nGRID')
    for z in grid:
        for x in z:
            print(''.join(x))
        print('')


def generation(grid):
    old = copy.deepcopy(grid)
    new = copy.deepcopy(grid)
    for z in range(len(old)):
        for x in range(len(old[0])):
            for y in range(len(old[0][0])):
                n = checkNeighbours(old, x, y, z)
                if old[z][x][y] == '#':
                    if n != 2 and n != 3:
                        new[z][x][y] = '.'
                elif old[z][x][y] == '.':
                    if n == 3:
                        new[z][x][y] = '#'
    # printgrid(new)
    return new


printgrid(grid)
old = copy.deepcopy(grid)
new = generation(old)
printgrid(new)

# old = copy.deepcopy(grid)
# # printgrid(old)
# new = generation(old)
#
# i = 0
# while i < 99:
#     old = copy.deepcopy(new)
#     new = generation(old)
#     i += 1
#
# on = 0
# for x in new:
#     on += x.count('#')
#
# print('solution to part 1:', on)