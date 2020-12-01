# Advent of Code 2019
# The IntCode saga
# Part 1: 2019 day 02

input = list(map(int, open('inputs/02.txt').read().split(',')))

# position in the list of integers separated by commas
# opcode [1, 2, 99] indicates what to do
# # 99: program is finished and should immediately halt
# # 1 : adds together numbers read from two positions and stores the result in a third position
# # # the first three integers immedately after the opcode tell you these three positions - the first two indicate the positions from which you should read the input values, and the third indicates the psition at which the output should be stored
# # 2 : multiplies the two inputs, otherwise works exactly like opcode 1

# Once you're done processing an opcode, move on to the next one by stepping forward 4 positions

# before running the program, replace position 1 with value 12 and replace position 2 with value 2.

input[1] = 12
input[2] = 2

def addition(input, first, second):
    return input[first] + input[second]


def multiplication(input, first, second):
    return input[first] * input[second]


i = 0

while input[i] != 99:
    opcode = input[i]
    if opcode == 1:
        input[input[i+3]] = addition(input, input[i+1], input[i+2])
    elif opcode == 2:
        input[input[i+3]] = multiplication(input, input[i+1], input[i+2])
    i += 4

print(input[0])
