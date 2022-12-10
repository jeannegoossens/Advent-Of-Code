inp = open('inputs/Day10.txt').read().split('\n')

X = 1
important = [19, 59, 99, 139, 179, 219]
active = False

signals = []

drawing = ''
drawidx = 0

for cycle in range(240):
    # draw CRT
    if abs(drawidx - X) <= 1:
        drawing += '#'
    else:
        drawing += '.'
    drawidx += 1
    if drawidx == 40:
        drawing += '\n'
        drawidx = 0

    # log important cycles
    if cycle in important:
        signals.append(X * (cycle+1))

    # process
    if active:
        X += active
        active = False
    elif inp[0].startswith('addx'):
        instr = inp.pop(0)
        active = int(instr.split()[-1])
    elif inp[0].startswith('noop'):
        instr = inp.pop(0)

print("part 1:", sum(signals))
print("part 2:")
print(drawing)
