import re

inp = [i for i in open("inputs/day04.txt").read().split('\n')]
sum = 0

for line in inp:
    print(line)
    items = list(re.search(r"(\b[a-z\-]+\b)\-(\b[0-9]+\b)\[(\b[a-z]+\b)\]", line).groups())
    name = items[0].replace('-', '')
    checksum = items[2]

    counts = {}
    for c in set(name):
        count = name.count(c)
        if count in counts.keys():
            counts[count].append(c)
        else:
            counts[count] = [c]

    realchecksum = ''

    for count in reversed(sorted(counts.keys())):
        realchecksum += ''.join(sorted(counts[count]))
    if checksum == realchecksum[:5]:
        sum += int(items[1])

print(sum)
