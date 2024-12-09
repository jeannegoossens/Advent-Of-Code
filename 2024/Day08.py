inp = open("inputs/Day08.txt").read()
antennas = set(inp)
antennas.remove('\n')
antennas.remove('.')

grid = [list(i) for i in inp.split('\n')]
gridsize = len(grid)
antinodes = set()

locations = {a: [] for a in antennas}

for row in range(len(grid)):
    for col in range(len(grid[0])):
        if grid[row][col] != '.':
            locations[grid[row][col]].append((row, col))

for antenna, instances in locations.items():
    for this in instances:
        for that in instances:
            if this != that:
                vector = (this[0] - that[0], this[1] - that[1])
                if 0 <= this[0] + vector[0] < gridsize:
                    if 0 <= this[1] + vector[1] < gridsize:
                        antinodes.add((this[0] + vector[0],this[1] + vector[1]))

print("Part 1:", len(antinodes))
