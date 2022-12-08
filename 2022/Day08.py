inp = [[int(i) for i in x] for x in open('inputs/Day08.txt').read().split('\n')]

visible = len(inp) * 2 + len(inp[0]) * 2 - 4
maxscenic = 0

for row in range(len(inp[1:-1])):
    row = row + 1
    for column in range(len(inp[row][1:-1])):
        column = column + 1
        tree = inp[row][column]
        visibility = [0, 0, 0, 0]
        scenicity = [0, 0, 0, 0]
        for t in inp[row+1:]:
            if tree <= t[column]:
                scenicity[0] += 1
                visibility[0] = 0
                break
            else:
                scenicity[0] += 1
                visibility[0] += 1
        for t in reversed(inp[:row]):
            if tree <= t[column]:
                scenicity[1] += 1
                visibility[1] = 0
                break
            else:
                scenicity[1] += 1
                visibility[1] += 1
        for t in inp[row][column+1:]:
            if tree <= t:
                scenicity[2] += 1
                visibility[2] = 0
                break
            else:
                scenicity[2] += 1
                visibility[2] += 1
        for t in reversed(inp[row][:column]):
            if tree <= t:
                scenicity[3] += 1
                visibility[3] = 0
                break
            else:
                scenicity[3] += 1
                visibility[3] += 1

        count = sum(scenicity)
        if count > 0:
            visible += 1

        scenic = scenicity[0] * scenicity[1] * scenicity[2] * scenicity[3]
        maxscenic = max(maxscenic, scenic)

print("part 1:", visible)
print("part 2:", maxscenic)
