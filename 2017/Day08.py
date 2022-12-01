inp = open('inputs/Day08.txt').read().split('\n')

registers = {}
maxever = 0

for line in inp:
    for r in registers.values():
        maxever = max(maxever, r)
    instructions = line.split()
    if instructions[4] not in registers.keys():
        registers[instructions[4]] = 0
    if instructions[0] not in registers.keys():
        registers[instructions[0]] = 0
    if instructions[1] == 'inc':
        if instructions[5] == '!=':
            if registers[instructions[4]] != int(instructions[6]):
                registers[instructions[0]] += int(instructions[2])
        elif instructions[5] == '==':
            if registers[instructions[4]] == int(instructions[6]):
                registers[instructions[0]] += int(instructions[2])
        elif instructions[5] == '>=':
            if registers[instructions[4]] >= int(instructions[6]):
                registers[instructions[0]] += int(instructions[2])
        elif instructions[5] == '>':
            if registers[instructions[4]] > int(instructions[6]):
                registers[instructions[0]] += int(instructions[2])
        elif instructions[5] == '<=':
            if registers[instructions[4]] <= int(instructions[6]):
                registers[instructions[0]] += int(instructions[2])
        elif instructions[5] == '<':
            if registers[instructions[4]] < int(instructions[6]):
                registers[instructions[0]] += int(instructions[2])
    elif instructions[1] == 'dec':
        if instructions[5] == '!=':
            if registers[instructions[4]] != int(instructions[6]):
                registers[instructions[0]] -= int(instructions[2])
        elif instructions[5] == '==':
            if registers[instructions[4]] == int(instructions[6]):
                registers[instructions[0]] -= int(instructions[2])
        elif instructions[5] == '>=':
            if registers[instructions[4]] >= int(instructions[6]):
                registers[instructions[0]] -= int(instructions[2])
        elif instructions[5] == '>':
            if registers[instructions[4]] > int(instructions[6]):
                registers[instructions[0]] -= int(instructions[2])
        elif instructions[5] == '<=':
            if registers[instructions[4]] <= int(instructions[6]):
                registers[instructions[0]] -= int(instructions[2])
        elif instructions[5] == '<':
            if registers[instructions[4]] < int(instructions[6]):
                registers[instructions[0]] -= int(instructions[2])


print(max(registers.values()))
print(maxever)
