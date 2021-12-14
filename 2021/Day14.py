template, pairs = open('inputs/day14.txt').read().split('\n\n')
pairs = {i.split(' -> ')[0]: i.split(' -> ')[1] for i in pairs.split('\n')}


def runSteps(polymer, steps):
    paircount = {pair: polymer.count(pair) for pair in pairs.keys()}
    lettercount = {letter: polymer.count(letter) for letter in set(list(''.join(pairs.keys())))}
    for i in range(steps):
        newpaircount = paircount.copy()
        for pair in paircount.keys():
            newstring = pair[0] + pairs[pair] + pair[1]
            lettercount[pairs[pair]] += paircount[pair]
            newpaircount[newstring[0]+newstring[1]] += paircount[pair]
            newpaircount[newstring[1]+newstring[2]] += paircount[pair]
            newpaircount[pair] -= paircount[pair]
        paircount = newpaircount
    return lettercount


polymer = runSteps(template, 10)
print('part 1:', max(polymer.values()) - min(polymer.values()))

polymer = runSteps(template, 40)
print('part 2:', max(polymer.values()) - min(polymer.values()))
