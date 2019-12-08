
from machine import Machine


def runprogram(sequence, numbers):  # 3,1,2,4,0
    nextinput = 0
    print('sequence', sequence)
    for phase in sequence:
        copynumbers = numbers.copy()
        print('current phase:', phase)
        m = Machine()
        nextinput = m.getvalue(copynumbers, phase, nextinput)
        print('phase', phase, 'outputs:', nextinput)
    return nextinput


def trysequences(numbers):
    return runprogram([1,0,4,3,2], numbers)


numbers = open('input.txt').read().split(',')
numbers = [int(i) for i in numbers]
print(len(numbers))

print(trysequences(numbers))

# numbers : 3,8,1001,8,10,8,105,1,0,0
#
#         3          1          2          4          0
#     O-------O  O-------O  O-------O  O-------O  O-------O
# 0 ->| Amp A |->| Amp B |->| Amp C |->| Amp D |->| Amp E |-> (to thrusters)
#     O-------O  O-------O  O-------O  O-------O  O-------O
