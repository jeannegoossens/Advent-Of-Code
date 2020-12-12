input = open('input.txt').read().split('\n')

x = 0
y = 0
compass = ['north', 'east', 'south', 'west']
facing = 'east'

for instruction in input:
    direction, distance = instruction[0], int(instruction[1:])
    if direction == 'L':
        facing = compass[compass.index(facing) - int(distance/90)]
    elif direction == 'R':
        turn = int(distance / 90)
        current = compass.index(facing)
        new = current + turn
        if new > 3:
            new = new - 4
        facing = compass[new]
    elif direction == 'N':
        y += distance
    elif direction == 'E':
        x += distance
    elif direction == 'S':
        y -= distance
    elif direction == 'W':
        x -= distance
    elif direction == 'F':
        if facing == 'north':
            y += distance
        elif facing == 'east':
            x += distance
        elif facing == 'south':
            y -= distance
        elif facing == 'west':
            x -= distance

print('solution to part 1:', abs(x) + abs(y))