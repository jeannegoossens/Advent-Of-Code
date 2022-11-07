inp = [i for i in open("inputs/day12.txt").read().split('\n')]

registers = {'a': 0, 'b': 0, 'c': 1, 'd': 0}
idx = 0

while idx < len(inp):
    instructions = inp[idx].split()
    if instructions[0] == 'cpy':
        if instructions[1].isalpha():
            registers[instructions[2]] = registers[instructions[1]]
        elif instructions[1].isnumeric():
            registers[instructions[2]] = int(instructions[1])
    elif instructions[0] == 'inc':
        registers[instructions[1]] += 1
    elif instructions[0] == 'dec':
        registers[instructions[1]] -= 1
    elif instructions[0] == 'jnz':
        if instructions[1].isnumeric() and instructions[1] == '0':
            idx+=1
        elif instructions[1].isalpha() and registers[instructions[1]] == 0:
            idx+=1
        else:
            idx += int(instructions[2])
        continue
    idx += 1

print(registers)
