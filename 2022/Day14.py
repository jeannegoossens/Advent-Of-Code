inp = open('inputs/Day14.txt').read().split('\n')

rocks = set()

# get the coordinates of all the rocks
for line in inp:
    coordinates = [tuple([int(j) for j in i.split(',')]) for i in line.split(' -> ')]
    for c in range(len(coordinates)-1):
        path = coordinates[c:c+2]
        if path[0][0] != path[1][0]:
            for x in range(min(path[1][0], path[0][0]), max(path[1][0], path[0][0])+1):
                for y in range(min(path[0][1], path[1][1]), max(path[0][1], path[1][1])+1):
                    rocks.add((x, y))
        elif path[0][1] != path[1][1]:
            for y in range(min(path[0][1], path[1][1]), max(path[0][1], path[1][1])+1):
                for x in range(min(path[0][0], path[1][0]), max(path[0][0], path[1][0])+1):
                    rocks.add((x, y))


def printit():
    print()
    for y in range(0, rockrange[1][1]+3):
        row = ''
        for x in range(rockrange[0][0]-1, rockrange[0][1]+2):
            if (x, y) == entrypoint:
                row += '+'
            elif (x, y) in rocks:
                row += '#'
            elif (x, y) in settled:
                row += 'O'
            else:
                row += '.'
        print(row)
    print('#' * 60)


# determine the field size for printing
rockrange = (
    (min([r[0] for r in rocks]),
     max([r[0] for r in rocks])),
    (min([r[1] for r in rocks]),
     max([r[1] for r in rocks]))
)

rockbottom = max([r[1] for r in rocks]) + 2

# let's consider the rocks as the first settled sand
settled = set([r for r in rocks])

entrypoint = (500, 0)

freefall = False
hitentry = False
part1 = False

while not hitentry:
    # create a new grain of sand
    grain = entrypoint
    settledgrain = False

    while not settledgrain:
        # check below
        if (grain[0], grain[1]+1) in settled or grain[1]+1 == rockbottom:
            # check below, left
            if (grain[0] - 1, grain[1] + 1) in settled or grain[1]+1 == rockbottom:
                # check below, right
                if (grain[0] + 1, grain[1] + 1) in settled or grain[1]+1 == rockbottom:
                    # consider this grain settled
                    settled.add(grain)
                    settledgrain = True
                    if grain == entrypoint:
                        hitentry = True
                        print("part 2:", len(settled) - len(rocks))
                else:
                    # move it down and right
                    grain = (grain[0] + 1, grain[1] + 1)
            else:
                # move it down and left
                grain = (grain[0] - 1, grain[1] + 1)
        else:
            # move it down
            grain = (grain[0], grain[1] + 1)

        # if there's no settled item left with the same x and a higher y
        if not part1 and len([s for s in settled if s[0] == grain[0] and s[1] > grain[1]]) < 1:
            freefall = True
            part1 = len(settled) - len(rocks)
            print("part 1:", len(settled) - len(rocks))
