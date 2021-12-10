# Advent of Code 2019
# The IntCode saga
# Part 1: 2019 day 02


def run(intcode, inputvalue = 5):
    opcode = 0
    while intcode[opcode] != 99:
        instruction = str(intcode[opcode]).zfill(5)
        op = int(instruction[-2:])
        p1mode = int(instruction[-3])
        p2mode = int(instruction[-4])
        p3mode = int(instruction[-5])
        if intcode[opcode] == 1:
            p1 = intcode[intcode[opcode+1]] if p1mode == 0 else intcode[opcode+1]
            p2 = intcode[intcode[opcode+2]] if p2mode == 0 else intcode[opcode+2]
            if p3mode == 0:
                intcode[intcode[opcode+3]] = p1 + p2
            else:
                intcode[opcode+3] = p1 + p2
            opcode += 4
        elif intcode[opcode] == 2:
            p1 = intcode[intcode[opcode+1]] if p1mode == 0 else intcode[opcode+1]
            p2 = intcode[intcode[opcode+2]] if p2mode == 0 else intcode[opcode+2]
            if p3mode == 0:
                intcode[intcode[opcode+3]] = p1 * p2
            else:
                intcode[opcode+3] = p1 * p2
            opcode += 4
        elif intcode[opcode] == 3:
            if p1mode == 0:
                intcode[intcode[opcode+1]] = inputvalue
            else:
                intcode[opcode+1] = inputvalue
            opcode += 2
        elif intcode[opcode] == 4:
            if p1mode == 0:
                print(intcode[intcode[opcode+1]])
            else:
                print(intcode[opcode+1])
            opcode += 2
    return intcode[0]


inp = [int(i) for i in open('inputs/05.txt').read().split(',')]
print(inp)


def findanswer():
    intcode = [int(i) for i in open('inputs/05.txt').read().split(',')]
    #intcode = [1002,4,3,4,33]
    inputnumber = int(input('What id? '))
    answer = run(intcode, inputnumber)
print(findanswer())
