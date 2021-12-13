coordinates, folds = open('inputs/day13.txt').read().split('\n\n')

coordinates = [(int(i.split(',')[0]), int(i.split(',')[1])) for i in coordinates.split('\n')]
folds = [(i.split(' ')[2].split('=')[0], int(i.split(' ')[2].split('=')[1])) for i in folds.split('\n')]


def runFold(coordinates, fold):
    level = fold[1]

    if fold[0] == 'y':
        for coordinate in range(len(coordinates)):
            c = coordinates[coordinate]
            if c[1] > level:
                distance = abs(c[1] - level)
                coordinates[coordinate] = (c[0], level - distance)
    elif fold[0] == 'x':
        for coordinate in range(len(coordinates)):
            c = coordinates[coordinate]
            if c[0] > level:
                distance = abs(c[0] - level)
                coordinates[coordinate] = (level - distance, c[1])
    return coordinates


# part 1: get the first fold
print('part 1:', len(set(runFold(coordinates, folds[0]))))

# part 2: get all folds
for f in folds:
    coordinates = runFold(coordinates, f)

for y in range(6):
    row = ''
    for x in range(39):
        if (x,y) in coordinates:
            row += '#'
        else:
            row += ' '
    print(row)
