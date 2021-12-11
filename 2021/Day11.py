inp = [[int(i) for i in j] for j in open('inputs/day11.txt').read().split('\n')]


def checkForFlashers(grid):
    for j in [i for x in grid for i in x]:
        if j > 9:
            return True
    return False


def step(grid, totalflashes):
    # first increase each octopus by 1
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            grid[y][x] += 1

    neighbours = [(-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (1, 1), (0, 1), (1, 0)]
    # if > 9: flash
    flashers = []
    while checkForFlashers(grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] > 9 and grid[y][x] not in flashers:
                    forbidden = []
                    if y == 0:
                        forbidden.extend([(-1,0), (-1,-1), (-1,1)])
                    if y == len(inp) - 1:
                        forbidden.extend([(1, 0), (1, -1), (1, 1)])
                    if x == 0:
                        forbidden.extend([(0, -1), (-1, -1), (1, -1)])
                    if x == len(inp[0]) - 1:
                        forbidden.extend([(0,1), (-1, 1), (1,1)])
                    flashers.append((y, x))
                    grid[y][x] = 0
                    for n in neighbours:
                        if n not in forbidden:
                            grid[y+n[0]][x+n[1]] += 1

    totalflashes += len(flashers)
    for f in flashers:
        grid[f[0]][f[1]] = 0

    if len(set([i for x in grid for i in x])) == 1:
        sync = True
    else:
        sync = False

    return grid, totalflashes, sync


totalflashes = 0
steps = 0
synced = False
# for _ in range(100):  # use for test case part 1 instead of while loop
while not synced:
    steps += 1
    inp, totalflashes, synced = step(inp, totalflashes)
    if steps == 100:
        print('part 1:', totalflashes)
print('part 2:', steps)
