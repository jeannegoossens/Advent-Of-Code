input = open('inputs/input13.txt').read().split('\n')

from itertools import permutations

people = {}
for line in input:
    line = line[:-1].split(' ')
    if line[2] == 'gain':
        h = int(line[3])
    else:
        h = -1 * int(line[3])
    if line[0] in people:
        people[line[0]][line[-1]] = h
    else:
        people[line[0]] = {line[-1]: h}


def findBest(people):
    m = 0
    for seating in permutations(people.keys()):
        t = 0
        for x in range(len(seating)):
            t += people[seating[x]][seating[x-1]] + people[seating[x-1]][seating[x]]
        if t > m:
            m = t
    return m

print('solution to part 1:', findBest(people))

people['me'] = {}
for x in people.keys():
    people['me'][x] = 0
    people[x]['me'] = 0
print('solution to part 2:', findBest(people))