# 2015
# Day 14

input = open('inputs/input14.txt')

input = input.split('\n')

animals = {}

for deer in input:
    y = deer.split(' ')
    animals[y[0]] = {'speed': int(y[3]), 'length': int(y[6]), 'rest': int(y[13]), 'status': 'running', 'stamina': int(y[6]), 'position': 0, 'points': 0}

print('PART 1:')

for reindeer, stats in animals.items():
    # distance = ticks % (stats['length'] + stats['rest'])
    distance = 0
    ticks = 2503
    # print(reindeer, distance, stats['length'])
    while ticks > 0 and ticks > stats['length']:
        distance += stats['length'] * stats['speed']
        ticks = ticks - stats['length']
        if ticks < 0:
            distance = distance + abs(distance) * stats['speed']
        ticks = ticks - stats['rest']

    print(reindeer, distance)

print('\nPART 2:')
ticks = 2503
for tick in range(ticks):
    for reindeer, stats in animals.items():
        if stats['status'] == 'running':
            stats['position'] += stats['speed']
        stats['stamina'] -= 1
        if stats['stamina'] == 0:
            if stats['status'] == 'running':
                stats['stamina'] = stats['rest']
                stats['status'] = 'resting'
            else:
                stats['stamina'] = stats['length']
                stats['status'] = 'running'
    positions = [(k, v['position']) for k,v in animals.items()]
    first = max([x[1] for x in positions])
    for deer in positions:
        if deer[1] == first:
            animals[deer[0]]['points'] += 1

for reindeer, stats in animals.items():
    print(reindeer, stats['points'])