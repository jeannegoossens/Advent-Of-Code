import copy
inp = open("inputs/day3.txt").read().split('\n')

gamma = ''
epsilon = ''


def get_position_count(binaries):
    positions = [[0, 0] for i in range(len(inp[0]))]
    for p in range(len(positions)):
        for binary in binaries:
            positions[p][int(binary[p])] += 1
    return positions


positions = get_position_count(inp)
for p in range(len(positions)):
    gamma += str(positions[p].index(max(positions[p])))
    epsilon += str(positions[p].index(min(positions[p])))
print("part 1", int(gamma, 2) * int(epsilon, 2))
# 3901196

oxygen = copy.deepcopy(inp)
co2 = copy.deepcopy(inp)


def find_binary(binaries, comparison, equal):
    for p in range(len(binaries[0])):
        positions = get_position_count(binaries)
        if len(binaries) == 1:
            return binaries[0]
        else:
            character = equal
            if comparison == 'max' and positions[p][0] != positions[p][1]:
                character = str(positions[p].index(max(positions[p])))
            elif comparison == 'min' and positions[p][0] != positions[p][1]:
                character = str(positions[p].index(min(positions[p])))
        new = []
        for binary in binaries:
            if binary[p] == character:
                new.append(binary)
        binaries = new
    return binaries[0]


oxygen = find_binary(oxygen, 'max', '1')
co2 = find_binary(co2, 'min', '0')
print("part 2", int(co2, 2) * int(oxygen, 2))
# 4412188
