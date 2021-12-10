input = open('inputs/day02.txt').read().split('\n')

grid = [[1], [2,3,4], [5,6,7,8,9], ['A','B','C'], ['D']]

position = 5

def move(position, direction):
    if direction == 'U':
        if position in [1,2,4,5,9]:
            return position
        else:
            return position - 3
    elif direction == 'L':
        if position in [1,2,5,'A','D']:
            return position
        else:
            return position - 1
    elif direction == 'R':
        if position in [1,4,9,'C','D']:
            return position
        else:
            return position + 1
    elif direction == 'D':
        if position in [5,'A','D','C',9]:
            return position
        else:
            return position + 3

for line in input:
    for direction in line:
        position = move(position, direction)
    print(position)