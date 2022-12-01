inp = open('inputs/Day18.txt').read().split('\n')
registers = {}

# inp = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2""".split('\n')

sound = 'hello'

idx = 0

while 0 <= idx < len(inp):
    instr = inp[idx].split()
    if instr[0] == 'snd':
        sound = registers[instr[1]]
    elif instr[0] == 'set':
        if instr[2].isalpha():
            registers[instr[1]] = registers[instr[2]]
        else:
            registers[instr[1]] = int(instr[2])
    elif instr[0] == 'add':
        if instr[2].isalpha():
            registers[instr[1]] += registers[instr[2]]
        else:
            registers[instr[1]] += int(instr[2])
    elif instr[0] == 'mul':
        if instr[1] not in registers.keys():
            registers[instr[1]] = 1
        if instr[2].isalpha():
            registers[instr[1]] *= registers[instr[2]]
        else:
            registers[instr[1]] *= int(instr[2])
    elif instr[0] == 'mod':
        if instr[2].isalpha():
            registers[instr[1]] %= registers[instr[2]]
        else:
            registers[instr[1]] %= int(instr[2])
    elif instr[0] == 'rcv':
        if instr[1] not in registers.keys():
            registers[instr[1]] = 0
        if registers[instr[1]] != 0:
            print(sound)
            if type(sound) == int:
                break
    elif instr[0] == 'jgz':
        if instr[1].isnumeric():
            v = int(instr[1])
        else:
            v = registers[instr[1]]
        if v > 0:
            if instr[2].isalpha():
                idx += registers[instr[2]]
            else:
                idx += int(instr[2])
            continue
    idx += 1

print(sound)