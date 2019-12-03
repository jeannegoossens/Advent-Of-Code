lines = open("input.txt").read().split('\n')


def trackCoordinates(instruction, recent):
    # take the most recent location and the next instruction
    # get all the coordinates the wire passes with this instruction
    direction = instruction[0]
    distance = int(instruction[1:])
    x = recent[1]
    y = recent[0]
    path = []
    for i in range(distance):
        if direction == 'D':
            y -= 1
        elif direction == 'U':
            y += 1
        elif direction == 'R':
            x += 1
        elif direction == 'L':
            x -= 1
        path.append((y,x))
    return path


def trackPath(wire):
    # process all instructions given for a wire and return its full path
    path = [(0,0)]
    for x in wire:
        recent = path[-1]
        path.extend(trackCoordinates(x, recent))
    return path


def findIntersection(path1, path2):
    # find all intersections between the wires
    # minus the point of origin
    return list(set(path1).intersection(path2)).remove((0,0))


def manhattan(intersection, origin):
    # find the manhattan distance to the origin for an intersection
    return abs(origin[1] - intersection[1]) + abs(origin[0] + intersection[0])


def findClosestManhattan(wireInstructions1, wireInstructions2):
    # track the full paths of both wires
    wirepath1 = trackPath(wireInstructions1)
    wirepath2 = trackPath(wireInstructions2)

    # find all intersections between the wires
    intersections = findIntersection(wirepath1, wirepath2)

    # find the manhattan distance for every intersection
    manhattans = []
    for i in intersections:
        manhattans.append(manhattan(i, (0, 0)))

    # return the lowest manhattan distance
    return min(manhattans)


wireInstructions1 = lines[0].split(',')
wireInstructions2 = lines[1].split(',')

print(findClosestManhattan(wireInstructions1, wireInstructions2))
