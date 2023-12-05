inp = open('inputs/Day05.txt').read().split('\n\n')
seeds = [int(i) for i in inp[0].split(': ')[1].split(' ')]

toLocation = [[[int(y) for y in x.split(' ')] for x in z.split(':\n')[1].split('\n') ] for z in inp[1:]]


def process(seed, step):
    for seedrange in step:
        if seedrange[1] <= seed <= seedrange[1] + seedrange[2]:
            return seedrange[0] + (seed - seedrange[1])
    return seed


seedlocations = []
for seed in seeds:
    for step in toLocation:
        seed = process(seed, step)
    seedlocations.append(seed)

print(min(seedlocations))
