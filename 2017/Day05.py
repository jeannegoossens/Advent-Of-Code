inp = [int(i) for i in open('inputs/Day05.txt').read().split('\n')]
print(inp)

idx = 0
steps = 0
while 0 <= idx < len(inp):
    steps += 1
    instruction = inp[idx]
    if instruction >= 3:
        inp[idx] -= 1
    else:
        inp[idx] += 1
    idx += instruction
print(steps)