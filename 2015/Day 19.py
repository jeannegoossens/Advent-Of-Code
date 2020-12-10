input = open('inputs/input19.txt').read().split('\n\n')

import re

molecule = input[1]
replacements = input[0].split('\n')

creations = []

for replacement in replacements:
    from_atom, to_atom = replacement.split(' => ')
    for i in range(len(molecule)):
        if re.search(from_atom, molecule[i:]):
            new = molecule[:i] + re.sub(from_atom, to_atom, molecule[i:], 1)
            creations.append(new)

print('solution to part 1: ', len(list(set(creations))))

electron = 'e'
