# Advent of Code 2019
# The IntCode saga
# Part 1: 2019 day 02

# position in the list of integers separated by commas
# opcode [1, 2, 99] indicates what to do
# # 99: program is finished and should immediately halt
# # 1 : adds together numbers read from two positions and stores the result in a third position
# # # the first three integers immedately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the psition at which the output should be stored
# # 2 : multiplies the two inputs, otherwise works exactly like opcode 1

# Once you're done processing an opcode, move on to the next one by stepping forward 4 positions

# before running the program, replace position 1 with value 12 and replace position 2 with value 2.


def addition(input, first, second):
    return input[first] + input[second]


def multiplication(input, first, second):
    return input[first] * input[second]


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