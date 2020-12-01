input = 33100000

import numpy
houses = numpy.zeros(input, dtype=int)

for elf in range(1, input):
    houses[elf:elf*50:elf] += 11 * elf
    if houses[elf] >= input:
        print(elf)
        break