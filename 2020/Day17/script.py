import copy

grid = open('input.txt').read().split('\n')

# a b c         i j k           r s t
# d . e         l m n           u v w
# f g h         o p q           x y z


neighbours = {'a': (-1, -1, 0),  'b': (-1, 0, 0),  'c': (-1, 1, 0),
              'd': (0, -1, 0),                     'e': (0, 1, 0),
              'f': (1, -1, 0),   'g': (1, 0, 0),   'h': (1, 1, 0),

              'i': (-1, -1, -1), 'j': (-1, 0, -1), 'k': (-1, 1, -1),
              'l': (0, -1, -1),  'm': (0, 0, -1),  'n': (0, 1, -1),
              'o': (1, -1, -1),  'p': (1, 0, -1),  'q': (1, 1, -1),

              'r': (-1, -1, 1),  's': (-1, 0, 1),  't': (-1, 1, 1),
              'u': (0, -1, 1),   'v': (0, 0, 1),   'w': (0, 1, 1),
              'x': (1, -1, 1),   'y': (1, 0, 1),   'z': (1, 1, 1)}


def getInitialState(grid):
    active = []
    for line in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[line][c] == '#':
                active.append((line, c, 0))
    return active


def check_neighbours(active, coordinate, neighbours):
    occupied = 0
    for c in neighbours.values():
        if (coordinate[0] + c[0], coordinate[1] + c[1], coordinate[2] + c[2]) in active:
            occupied += 1
    return occupied


def generation(active, neighbours):
    old = copy.deepcopy(active)
    new = []
    for a in old:
        n = check_neighbours(old, a, neighbours)
        # first check for all existing actives
        if n == 2 or n == 3:
            new.append(a)
        # then check for all surrounding neighbours of that one
        for nbc in neighbours.values():
            neighbour = (a[0] + nbc[0], a[1] + nbc[1], a[2] + nbc[2])
            if neighbour not in old:
                nbn = check_neighbours(old, neighbour, neighbours)
                if nbn == 3:
                    new.append(neighbour)
    return new


def printgrid(grid, gen):
    minx = min([item[0] for item in grid])
    maxx = max([item[0] for item in grid])
    miny = min([item[1] for item in grid])
    maxy = max([item[1] for item in grid])
    minz = min([item[2] for item in grid])
    maxz = max([item[2] for item in grid])
    print('\ngeneration', gen, '(', countActive(grid), ')')
    for i in range(minz,maxz+1):
        print('\nz=', i)
        for j in range(minx, maxx+1):
            row = ''
            for k in range(miny, maxy+1):
                if ((j,k,i) in grid):
                    row += '#'
                else:
                    row += '.'
            print(row)


def countActive(grid):
    return len(set(grid))


active = getInitialState(grid)
i = 0
while i < 6:
    active = generation(active, neighbours)
    i += 1

print('solution to part 1:', countActive(active))
# 252 part 1
