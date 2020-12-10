input = open('inputs/input07.txt').read().split('\n')

import re
data = {}

for line in input:
    line = line.split(' -> ')
    data[line[1]] = line[0]

print(data)
level = 0

def find(code):
    global level
    command = data[code]
    signal = re.findall('[A-Z]+', command)
    wires = re.findall('[a-z0-9]+', command)
    for x in range(len(wires)):
        if wires[x].isnumeric():
            wires[x] = int(wires[x])
        elif wires[x].isalpha():
            level += 1
            check = find(wires[x].strip())
            wires[x] = check
            if type(check) == int:
                data[code] = str(check)
            level -= 1
        else:
            print(wires[x], 'not number or letter')

    if not signal:
        return wires[0]
    elif signal[0] == 'AND':
        return wires[0] & wires[1]
    elif signal[0] == 'OR':
        return wires[0] | wires[1]
    elif signal[0] == 'NOT':
        return ~wires[0] & 0xffff
    elif signal[0] == 'LSHIFT':
        return wires[0] << wires[1]
    elif signal[0] == 'RSHIFT':
        return wires[0] >> wires[1]
    else:
        print(code, command, 'ERROR')
        raise IndexError


print('solution to part 1:', find('a'))
