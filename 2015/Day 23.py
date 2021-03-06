input = open('inputs/input23.txt').read()

input = input.split('\n')

registers = {'a': 1, 'b': 0}
y = 0

while True:
    try:
        instructions = input[y].replace(',', '').split(' ')
    except IndexError:
        print(registers)
        break

    y += 1
    if instructions[0] == 'inc':
        registers[instructions[1]] += 1
    elif instructions[0] == 'hlf':
        registers[instructions[1]] = registers[instructions[1]] / 2
    elif instructions[0] == 'tpl':
        registers[instructions[1]] = registers[instructions[1]]*3
    elif instructions[0] == 'jmp':
        y += -1 + int(instructions[1])
    elif instructions[0] == 'jie' and (registers[instructions[1]] % 2 == 0):
        y += -1 + int(instructions[2])
    elif instructions[0] == 'jio' and registers[instructions[1]] == 1:
        y += -1 + int(instructions[2])