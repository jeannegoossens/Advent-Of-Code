inp = open('inputs/infi_input.txt').read().split('\n')

orientations = [(1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)]

orientation = 0
position = (0, 0)
footprints = set()

for line in inp:
    if line.startswith('draai'):
        rotation = int(line.split(' ')[-1]) // 45
        orientation = (orientation + rotation + len(orientations)) % len(orientations)
    else:
        for x in range(abs(int(line.split(' ')[-1]))):
            direction = orientations[orientation]
            if int(line.split(' ')[-1]) > 0:
                position = (position[0] + direction[0], position[1] + direction[1])
            else:
                position = (position[0] - direction[0], position[1] - direction[1])
            if line.startswith('loop'):
                footprints.add(position)
        footprints.add(position)

print("part 1:", abs(position[0]) + abs(position[1]))

print("part 2:")
for y in range(max([w[0] for w in footprints]), -1, -1):
    print(''.join(['#' if (y, x) in footprints else ' ' for x in range(max([w[1] for w in footprints]) + 1)]))
