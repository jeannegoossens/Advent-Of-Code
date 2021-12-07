import numpy as np

crabs = [int(i) for i in open("inputs/day7.txt").read().split(',')]
crabs = np.array(crabs)

minfuel = sum(crabs)
for position in range(min(crabs), max(crabs)+1):
    fuel = sum(abs(crabs - position))
    minfuel = min(minfuel, fuel)
print(minfuel)
