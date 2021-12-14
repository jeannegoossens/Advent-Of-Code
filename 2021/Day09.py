inp = [[int(i) for i in list(x)] for x in open("inputs/day09.txt").read().split('\n')]

generalneighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]

totalsum = 0
lowpoints = []

for y in range(len(inp)):
    for x in range(len(inp[0])):
        totalneighbours = 0
        neighbours = generalneighbours.copy()
        if y == 0:
            neighbours.remove((-1,0))
        if y == len(inp)-1:
            neighbours.remove((1,0))
        if x == 0:
            neighbours.remove((0,-1))
        if x == len(inp[0])-1:
            neighbours.remove((0,1))
        for n in neighbours:
            if inp[y+n[0]][x+n[1]] > inp[y][x]:
                totalneighbours += 1
        if len(neighbours) == totalneighbours:
            lowpoints.append((y,x))
            totalsum += 1 + inp[y][x]
print('part 1:', totalsum)

# part 2
basins = {c: [] for c in lowpoints}

# for every point in the grid that is not 9
for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] != 9:
            # keep moving over to lower neighbours until we reach one of the lowest points
            # now we know for this point in the grid to which basin it belongs
            og = (y,x)
            point = (y,x)
            while point not in lowpoints:
                for n in generalneighbours:
                    neighbour = (point[0] + n[0], point[1] + n[1])
                    if 0 <= neighbour[0] < len(inp) and 0 <= neighbour[1] < len(inp[0]):
                        if inp[neighbour[0]][neighbour[1]] < inp[point[0]][point[1]]:
                            point = neighbour
                            continue
            basins[point].append(og)

sizes = sorted([len(v) for v in basins.values()])[-3:]
print('part 2:', sizes[0] * sizes[1] * sizes[2])
