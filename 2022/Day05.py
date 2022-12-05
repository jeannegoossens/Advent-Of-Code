import re


def cleanline(line):
    line = re.sub(r'[\s]{2,4}', '  ', line)
    line = re.sub(']|\[', '', line)
    line = line[::2]
    return line.ljust(9)


def transpose(l1):
    l2 = [list(reversed([row[i] for row in l1])) for i in range(len(l1[0]))]
    return l2


# clean and read start situation
# if I clean up the spaces and square brackets from the input
# then the start situation will be 9x9 (with some padding)
# which I can transpose easily
start, moves = open('inputs/Day05.txt').read().split('\n\n')
start = [cleanline(line) for line in start.split('\n')]

# clean moves
moves = [i.split(' ') for i in moves.split('\n')]

# setup stacks in dict
stacks = {}
start = transpose(start)
for i in range(len(start)):
    stacks[i+1] = [i for i in start[i][1:] if i != ' ']

# play out the moves
for line in moves:
    size = int(line[1])
    fromstack = int(line[3])
    tostack = int(line[5])
    idx = len(stacks[fromstack]) - int(size)

    # part 1
    # for i in range(size):
    #     crate = stacks[fromstack].pop(-1)
    #     stacks[tostack].append(crate)

    # part 2
    crate = stacks[fromstack][idx:]
    stacks[fromstack] = stacks[fromstack][:idx]
    stacks[tostack].extend(crate)

sol = ''.join([v[-1] for v in stacks.values()])
print(sol)
