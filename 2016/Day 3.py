input = [[int(x) for x in line.split(' ') if x != ''] for line in open('inputs/day03.txt').read().split('\n')]

def checkLine(triangle):
    if (triangle[0] + triangle[1]) <= triangle[2]:
        return False
    if (triangle[1] + triangle[2]) <= triangle[0]:
        return False
    if (triangle[2] + triangle[0]) <= triangle[1]:
        return False
    return True


valid = 0
for line in input:
    if checkLine(line):
        valid += 1
print('solution to part 1:', valid)

valid = 0
row = 0
while row < len(input):
    grid = [*zip(*input[row:row+3])]
    for i in range(3):
        if checkLine(grid[i]):
            valid += 1
    row += 3
print('solution to part 2:', valid)