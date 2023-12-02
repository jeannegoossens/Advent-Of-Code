inp = [i for i in open('inputs/Day02.txt').read().split('\n')]

cubes = {'red': 12, 'green': 13, 'blue': 14}

ids = set()
powers = 0

for line in inp:
    line = line.split(': ')
    id = line[0].split(' ')[1]
    sets = [set.split(', ') for set in line[1].split('; ')]

    colors = {'red': 0, 'green': 0, 'blue': 0}

    for set in sets:
        for combo in set:
            nr, color = combo.split(' ')
            # part 1
            if int(nr) > cubes[color]:
                ids.add(int(id))
            # part 2
            colors[color] = max(colors[color], int(nr))

    powers += colors['red'] * colors['green'] * colors['blue']

print(5050 - sum(ids))
print(powers)
