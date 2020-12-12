input = open('input.txt').read().split('\n')

ship_x = 0
ship_y = 0

waypoint_x = 10
waypoint_y = 1

compass = ['north', 'east', 'south', 'west']
facing = 'east'


def rotate_waypoint(w_x, w_y, direction, distance):
    for i in range(int(distance/90)):
        if direction == 'R':
            t = w_y
            w_y = w_x * -1
            w_x = t
        elif direction == 'L':
            t = w_y
            w_y = w_x
            w_x = t * -1
    return w_x, w_y


for instruction in input:
    direction, distance = instruction[0], int(instruction[1:])
    if direction in ['L', 'R']:
        waypoint_x, waypoint_y = rotate_waypoint(waypoint_x, waypoint_y, direction, distance)
    elif direction == 'N':
        waypoint_y += distance
    elif direction == 'E':
        waypoint_x += distance
    elif direction == 'S':
        waypoint_y -= distance
    elif direction == 'W':
        waypoint_x -= distance
    elif direction == 'F':
        ship_x += distance * waypoint_x
        ship_y += distance * waypoint_y

print('solution to part 2:', abs(ship_x) + abs(ship_y))
