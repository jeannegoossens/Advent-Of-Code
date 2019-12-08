
from machine import Machine


def runprogram(sequence, numbers):  # 3,1,2,4,0
    nextinput = 0
    print('sequence', sequence)
    for amp in sequence:
        copynumbers = numbers
        print('current setting:', amp)
        m = Machine()
        nextinput = m.getvalue(copynumbers, 0, (amp, nextinput))
        print('outputs:', nextinput)
    return nextinput


def trysequences(numbers):
    return runprogram([3, 1, 2, 4, 0], numbers)


numbers = open('input.txt').read().split(',')
numbers = [int(i) for i in numbers]

print(trysequences(numbers))
