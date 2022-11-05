inp = [i for i in open("inputs/day08.txt").read().split('\n')]


def printscreen(active):
    for row in range(6):
        r = []
        for cell in range(50):
            if (row, cell) in active:
                r.append('#')
            else:
                r.append('.')
        print(''.join(r))


active = set()

for line in inp:
    commands = line.split()
    command = commands[0]
    if command == 'rect':
        newactive = active
        dimensions = [int(i) for i in commands[1].split('x')]
        for row in range(dimensions[1]):
            for cell in range(dimensions[0]):
                newactive.add((row, cell))
    elif command == 'rotate':
        newactive = set()
        idx = int(commands[2].split('=')[1])
        steps = int(commands[-1])
        if commands[1] == 'row':
            for cell in active:
                if cell[0] == idx:
                    new = (cell[0], (cell[1] + steps) % 50)
                    newactive.add(new)
                else:
                    newactive.add(cell)

        elif commands[1] == 'column':
            for cell in active:
                if cell[1] == idx:
                    new = ((cell[0] + steps) % 6, cell[1])
                    newactive.add(new)
                else:
                    newactive.add(cell)

    active = newactive

printscreen(active)
print("part 1:", len(active))
# part 2: ZFHFSFOGPO
