import itertools
from machine import Machine


def runprogram(sequence, numbers):  # 3,1,2,4,0
    nextinput = 0
    for phase in sequence:
        copynumbers = numbers.copy()
        m = Machine()
        nextinput = m.getvalue(copynumbers, phase, nextinput)
    return nextinput


def trysequences(numbers):
    sequences = list(itertools.permutations([0,1,2,3,4]))
    highest = 0
    copynumbers = numbers.copy()
    for s in sequences:
        result = runprogram(s, copynumbers)
        if result > highest:
            highest = result
        print(s, highest)
    return highest


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
