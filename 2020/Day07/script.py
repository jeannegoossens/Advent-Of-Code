input = open('input.txt').read().split('\n')

import re

pt1 = {}
pt2 = {}

for line in input:
    outer, inner = line.split(r' bags contain ')
    pt2[outer] = {}

    bags = re.split(' bags, | bag, | bag | bags | bags\.| bag\.', inner)[:-1]
    if bags[0] == 'no other':
        continue

    inside = [(bag[2:], int(re.findall('[0-9]+', bag)[0])) for bag in bags]

    # construct outside -> inwards
    pt2[outer] = {bag[0]: bag[1] for bag in inside}

    # construct inside -> outwards
    for bag in inside:
        if bag[0] in pt1.keys():
            pt1[bag[0]][outer] = bag[1]
        else:
            pt1[bag[0]] = {outer: bag[1]}
    if not(outer in pt1.keys()):
        pt1[outer] = {}


def checkOutside(bag):
    inside = pt1[bag]
    for bag, amount in inside.items():
        total_bags.append(bag)
        checkOutside(bag)
    return


def checkInside(color):
    inside = pt2[color]
    if inside is None:
        return 0
    else:
        return sum([inside[amount] * checkInside(amount) + inside[amount] for amount in inside])


total_bags = []
checkOutside('shiny gold')
print('solution to part 1:', len(set(total_bags)))
print('solution to part 2:', checkInside('shiny gold'))
