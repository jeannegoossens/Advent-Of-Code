input = open('input.txt').read().split('\n')

import re
from itertools import product
mem = {}
mask = ''.join(['X' for _ in range(36)])
for line in input:
    if line.startswith('mask'):
        mask = line.split(' ')[2]
    else:
        index = int(re.findall('\[(.*)\]', line)[0])
        number = int(re.findall(' = (.*)', line)[0])
        number = '{:036b}'.format(number)
        for c in range(len(mask)):
            if mask[c] != 'X':
                number = number[:c] + mask[c] + number[c + 1:]
        mem[index] = int(number, 2)

print('solution to part 1:', sum([v for v in mem.values()]))


mem = {}
mask = ''.join(['X' for _ in range(36)])
for line in input:
    if line.startswith('mask'):
        mask = line.split(' ')[2]
    else:
        index = int(re.findall('\[(.*)\]', line)[0])
        number = int(re.findall(' = (.*)', line)[0])
        index = '{:036b}'.format(index)
        for c in range(len(mask)):
            if mask[c] != '0':
                index = index[:c] + mask[c] + index[c + 1:]

        n = index.count('X')
        ps = product([0, 1], repeat=n)
        # for every product of 0 and 1 of length n 'X'es:
        for p in ps:
            i = 0
            option = index
            for c in range(len(index)):
                if index[c] == 'X':
                    option = option[:c] + str(p[i]) + option[c + 1:]
                    i += 1
            mem[int(option, 2)] = number
print(mem)

print('solution to part 2:', sum([v for v in mem.values()]))