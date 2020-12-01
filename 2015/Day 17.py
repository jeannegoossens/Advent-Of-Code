input = """33
14
18
20
45
35
16
35
1
13
18
13
50
44
48
6
24
41
30
42"""

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