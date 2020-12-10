input = open('inputs/input17.txt').read()

import itertools

input = list(map(int, input.split('\n')))

result = []
for i in range(len(input), 0, -1):
    for seq in itertools.combinations(input, i):
        if sum(seq) == 150:
            result.append(seq)

print(result)
print(len(result))

minlength = 100
for option in result:
    minlength = min(len(option), minlength)

for option in result:
    if len(option) == minlength:
        print(option)