# Advent of Code 2019
# The IntCode saga
# Part 1: 2019 day 02


def addition(input, first, second):
    return input[first] + input[second]


def multiplication(input, first, second):
    return input[first] * input[second]


def takeInput(intcode, first):
    return first


def giveOutput(intcode, first):
    return intcode[first]


def run(intcode, noun, verb):
    intcode[1] = noun
    intcode[2] = verb
    i = 0
    while intcode[i] != 99:
        opcode = intcode[i]
        if opcode == 1:
            intcode[intcode[i+3]] = addition(intcode, intcode[i+1], intcode[i+2])
            i += 4
        elif opcode == 2:
            intcode[intcode[i+3]] = multiplication(intcode, intcode[i+1], intcode[i+2])
            i += 4
        elif opcode == 3:
            intcode[intcode[i+1]] = 000
            i += 2
        elif opcode == 4:
            giveOutput(intcode, intcode[i+1])
            i += 2
        else:
            print(intcode[i:i+4])
            i += 4
    return intcode[0]


input = list(map(int, open('inputs/02.txt').read().split(',')))

# part 1
noun = 12
verb = 2
print(run(input.copy(), noun, verb))

# part 2
for noun in range(0, 99):
    for verb in range(0, 99):
        intcode = input.copy()
        result = run(intcode, noun, verb)
        if result == 19690720:
            print(100*noun + verb)