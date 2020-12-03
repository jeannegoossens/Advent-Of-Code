input = open('input.txt').read().split('\n')


def checkRoute(horizontalstep, verticalstep, grid):
    trees = 0
    x = 0
    for row in grid[::verticalstep]:
        if row[x] == '#':
            trees += 1

        for i in range(horizontalstep):
            x += 1
            if x == len(row):
                x = 0
    return trees


tests = [(1,1), (3,1), (5,1), (7,1), (1,2)]

total = 1
for test in tests:
    total = total * checkRoute(test[0], test[1], input)

print('answer part 1:', checkRoute(3, 1, input))
print('answer part 2:', total)
