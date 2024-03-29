import re

inp = [i for i in open("inputs/day04.txt").read().split('\n')]
sum = 0
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for line in inp:
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

    decrypted = ''
    for char in items[0]:
        if char.isalpha():
            decrypted += alphabet[(alphabet.index(char) + int(items[1])) % 26]
        else:
            decrypted += char
    if decrypted == 'northpole-object-storage':
        print(f'part 2: {items[1]}')

print(f'part 1: {sum}')
