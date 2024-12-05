inp = open('inputs/Day04.txt').read().split('\n')
height = len(inp)
width = len(inp[0])

countXmas = 0
countMas = 0

for idxX, row in enumerate(inp):
    for idxY, cell in enumerate(row):
        if cell == 'X':
            # up left
            if 0 <= idxX - 3 < height and 0 <= idxY - 3 < width and \
                    inp[idxX - 1][idxY - 1] == 'M' and \
                    inp[idxX - 2][idxY - 2] == 'A' and \
                    inp[idxX - 3][idxY - 3] == 'S':
                countXmas += 1
            # up
            if 0 <= idxX - 3 < height and \
                    inp[idxX - 1][idxY] == 'M' and \
                    inp[idxX - 2][idxY] == 'A' and \
                    inp[idxX - 3][idxY] == 'S':
                    countXmas += 1
            # up right
            if 0 <= idxX - 3 < height and 0 <= idxY + 3 < width and \
                    inp[idxX - 1][idxY + 1] == 'M' and \
                    inp[idxX - 2][idxY + 2] == 'A' and \
                    inp[idxX - 3][idxY + 3] == 'S':
                    countXmas += 1
            # left
            if 0 <= idxY - 3 < width and \
                    inp[idxX][idxY - 1] == 'M' and \
                    inp[idxX][idxY - 2] == 'A' and \
                    inp[idxX][idxY - 3] == 'S':
                    countXmas += 1
            # right
            if 0 <= idxY + 3 < width and \
                    inp[idxX][idxY + 1] == 'M' and \
                    inp[idxX][idxY + 2] == 'A' and \
                    inp[idxX][idxY + 3] == 'S':
                    countXmas += 1
            # down left
            if 0 <= idxX + 3 < height and 0 <= idxY - 3 < width and \
                    inp[idxX + 1][idxY - 1] == 'M' and \
                    inp[idxX + 2][idxY - 2] == 'A' and \
                    inp[idxX + 3][idxY - 3] == 'S':
                    countXmas += 1
            # down
            if 0 <= idxX + 3 < height and\
                    inp[idxX + 1][idxY] == 'M' and \
                    inp[idxX + 2][idxY] == 'A' and \
                    inp[idxX + 3][idxY] == 'S':
                    countXmas += 1
            # down right
            if 0 <= idxX + 3 < height and 0 <= idxY + 3 < width and \
                    inp[idxX + 1][idxY + 1] == 'M' and \
                    inp[idxX + 2][idxY + 2] == 'A' and \
                    inp[idxX + 3][idxY + 3] == 'S':
                    countXmas += 1
        if cell == 'A':
            if 1 <= idxX < height - 1 and 1 <= idxY < width - 1:
                if (inp[idxX - 1][idxY - 1] == 'M' and inp[idxX + 1][idxY + 1] == 'S') or \
                        (inp[idxX - 1][idxY - 1] == 'S' and inp[idxX + 1][idxY + 1] == 'M'):
                    if (inp[idxX + 1][idxY - 1] == 'M' and inp[idxX - 1][idxY + 1] == 'S') or \
                            (inp[idxX + 1][idxY - 1] == 'S' and inp[idxX - 1][idxY + 1] == 'M'):
                        countMas += 1

print("Part 1:", countXmas)
print("Part 2:", countMas)
