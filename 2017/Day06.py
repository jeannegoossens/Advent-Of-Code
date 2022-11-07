inp = [int(i) for i in open('inputs/Day06.txt').read().split('\t')]
print(inp)

configurations = set()
configurations.add(' '.join([str(x) for x in inp]))
steps = 0

while True:
    steps += 1
    idx = inp.index(max(inp))
    nr = inp[idx]
    inp[idx] = 0
    for _ in range(nr):
        idx = (idx + 1) % len(inp)
        inp[idx] += 1
    if "10 9 8 7 6 5 4 3 1 1 0 15 14 13 11 12" == ' '.join([str(x) for x in inp]):
        print(steps)
    if ' '.join([str(x) for x in inp]) in configurations:
        print(' '.join([str(x) for x in inp]))
        break
    else:
        configurations.add(' '.join([str(x) for x in inp]))

print(steps)
print(7864 - 6169)
