inp = open('inputs/Day04.txt').read().split('\n')

containment = 0
overlap = 0

for line in inp:
    first, second = line.split(',')
    first = [int(i) for i in first.split('-')]
    second = [int(i) for i in second.split('-')]

    # part 1
    if first[0] <= second[0] and first[1] >= second[1] or second[0] <= first[0] and second[1] >= first[1]:
        containment += 1

    # part 2
    if len(set(list(range(first[0], first[1]+1))) & set(list(range(second[0], second[1]+1)))) > 0:
        overlap += 1

print("part 1:", containment)
print("part 2:", overlap)
