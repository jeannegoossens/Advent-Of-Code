grid = [[int(x) for x in y] for y in open('inputs/Day10.txt').read().split('\n')]

for row in grid:
    print(''.join([str(x) for x in row]))

print()

trailheads = set()

for row in range(len(grid)):
    for column in range(len(grid[0])):
        if grid[row][column] == 9:
            trailheads.add((row, column))

print("trailheads:\t", trailheads)

neighbours = {(0, 1), (0, -1), (1, 0), (-1, 0)}
scores = {t: set() for t in trailheads}


def find_path(history):
    current = history[-1]
    if grid[current[0]][current[1]] == 0:
        scores[current].add(history[0])
        print('found it:', history)
    for nb in neighbours:
        check = (current[0] + nb[0], current[1] + nb[1])
        if check not in history:
            if 0 <= check[0] < len(grid) and 0 <= check[1] < len(grid[0]):
                if abs(grid[check[0]][check[1]] - grid[current[0]][current[1]]) == 1:
                    history.append(check)
                    find_path(history)


for t in trailheads:
    find_path([t])


print("scores:\t\t", {x: len(y) for x, y in scores.items()})
print("sum:\t\t", sum([len(y) for y in scores.values()]))
