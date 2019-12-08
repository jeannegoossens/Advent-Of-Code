# SUMMARY OF THIS PROGRAM

# FROM DAY 2:
# position 1 = opcode
# position 2 = input 1 location
# position 3 = input 2 location
# position 4 = output location
#
# instruction pointer = address of current instruction (so the opcode basically)
#
# opcodes:
# 1 = sum (takes 3 parameters)
# 2 = multiply (takes 3 parameters)
# 3 = takes input, saves to first parameters address (takes 1 parameter)
# 4 = takes value of parameter, outputs it (takes 1 parameter)
# 5 = jump-if-true: if par1 is not zero, instruction pointer becomes the value of par2
# 6 = jump-if-false: if par1 is zero, instruction pointer becomes the value of par2
# 7 = less-than: if par1 < par2, then position.par3 = 1 else 0
# 8 = equals: if par1 == par2, then position.par3 = 1 else 0
#
# parameter modes:
# 0 = position mode - causes the parameter to be interpreted as a position
# 1 = immediate mode - parameter is interpreted as a value
#
# parameter mode is stored in same value as opcode:
# first 2 digits: opcode
# the other digits are the three parameters' parameter modes


from machine import Machine

m = Machine()


def runprogram(sequence, numbers):  # 3,1,2,4,0
    nextinput = 0
    for amp in sequence:
        copynumbers = numbers
        print(amp)
        m = Machine()
        nextinput = m.getvalue(copynumbers, 0, (amp, nextinput))
    return nextinput


def trysequences(numbers):
    return runprogram([3,1,2,4,0], numbers)


numbers = open('input.txt').read().split(',')
numbers = [int(i) for i in numbers]

print(trysequences(numbers))
