input = open('inputs/day02.txt').read().split('\n')

grid = [1,2,3,4,5,6,7,8,9,'A','B','C','D']

position = 4

#     1                 0
#   2 3 4             1 2 3
# 5 6 7 8 9         4 5 6 7 8
#   A B C             9 10 11
#     D                 12

def move(position, direction):
    if direction == 'U':
        if position in [0, 1, 3, 4, 8]:
            return position
        elif position in [2, 12]:
            return position - 2
        else:
            return position - 4
    elif direction == 'L':
        if position in [0, 1, 4, 9, 12]:
            return position
        else:
            return position - 1
    elif direction == 'R':
        if position in [0, 3, 8, 11, 12]:
            return position
        else:
            return position + 1
    elif direction == 'D':
        if position in [4, 9, 12, 11, 8]:
            return position
        elif position in [0, 10]:
            return position + 2
        else:
            return position + 4


code = ''
for line in input:
    for direction in line:
        position = move(position, direction)
    code += str(grid[position])
print(code)