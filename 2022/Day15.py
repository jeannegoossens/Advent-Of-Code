import re

inp = open('inputs/Day15.txt').read().split('\n')

sensors = []
beacons = []
manhattans = []
boundaries = ((0, 0), (1, 1))


def manhattan(pointa, pointb):
    return abs(pointa[0] - pointb[0]) + abs(pointa[1] - pointb[1])


for line in inp:
    groups = [int(i) for i in re.findall(r'([\-0-9]+)', line)]
    manh = manhattan((groups[0], groups[1]), (groups[2], groups[3]))
    manhattans.append(manh)
    sensors.append((groups[0], groups[1]))
    beacons.append((groups[2], groups[3]))
    boundaries = ((min(min(groups[::2]), boundaries[0][0]),
                   max(max(groups[::2]), boundaries[0][1])),
                  (min(min(groups[1::2]), boundaries[1][0]),
                   max(max(groups[1::2]), boundaries[1][1])))

print("sensors", sensors)
print("beacons", beacons)
print("manhattans", manhattans)
print("boundaries", boundaries)

y = 2_000_000

cannot = set()

for x in range(boundaries[0][0], boundaries[0][1]+1):
    for idx, s in enumerate(sensors):
        if manhattan((x, y), s) <= manhattans[idx] and (x, y) not in beacons:
            cannot.add(x)
            break

print(len(cannot))

# 4893542
# 4882032
# 4882031
# 4882030
# 7449389
