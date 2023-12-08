inp = open('inputs/Day08.txt').read().split('\n\n')

instructions = inp[0].replace("L", "0").replace("R", "1")
directions = {x.split(' = ')[0]: (x.split(' = ')[1][1:-2].split(', ')[0], x.split(' = ')[1][1:-1].split(', ')[1]) for x in inp[1].split('\n')}

print(instructions)
print(directions)

position = 'AAA'
steps = 0
total = 0

while position != 'ZZZ':
    position = directions[position][int(instructions[steps])]
    steps += 1
    if steps == len(instructions):
        total += steps
        steps = 0

print(total)
