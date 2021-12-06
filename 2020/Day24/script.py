inp = open('input.txt').read().split('\n')


def takestep(location, path):
    se = (-1, 1)
    ne = (1, 1)
    e = (0, 2)
    sw = (-1, -1)
    nw = (1, -1)
    w = (0, -2)

    if path.startswith('se'):
        step = se
        path = path[2:]
    elif path.startswith('ne'):
        step = ne
        path = path[2:]
    elif path.startswith('sw'):
        step = sw
        path = path[2:]
    elif path.startswith('nw'):
        step = nw
        path = path[2:]
    elif path.startswith('e'):
        step = e
        path = path[1:]
    elif path.startswith('w'):
        step = w
        path = path[1:]
    location = tuple(map(lambda i, j: i + j, location, step))
    return location, path


start = (0, 0)
flipped = []
paths = inp

for path in paths:
    location = start
    while len(path) > 0:
        location, path = takestep(location, path)
    if location in flipped:
        flipped.remove(location)
    else:
        flipped.append(location)
print('part 1:', len(flipped))


# part 2
def day(floor):
    neighbours = [(-1, 1), (1, 1), (0, 2), (-1, -1), (1, -1), (0, -2)]
    newfloor = []
    for tile in floor:
        active_neighbours = 0
        for neighbour in neighbours:
            if tuple(map(lambda i, j: i + j, tile, neighbour)) in floor:
                active_neighbours += 1
        if active_neighbours != 0 and active_neighbours <= 2:
            newfloor.append(tile)
        for neighbour in neighbours:
            active_neighbours = 0
            n = tuple(map(lambda i, j: i + j, tile, neighbour))
            for theirs in neighbours:
                if tuple(map(lambda i, j: i + j, n, theirs)) in floor:
                    active_neighbours += 1
            if active_neighbours == 2:
                newfloor.append(n)
    return list(set(newfloor))


floor = flipped
for x in range(100):
    floor = day(floor)
print('part 2:', len(floor))
