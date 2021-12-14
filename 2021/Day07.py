crabs = [int(i) for i in open("inputs/day07.txt").read().split(',')]

minfuel = sum(crabs)*sum(crabs)
for position in range(min(crabs), max(crabs)+1):
    # gaussian summation = n * (n + 1) / 2
    fuel = sum([abs(n - position) * (abs(n - position) + 1) / 2 for n in crabs])
    minfuel = min(minfuel, int(fuel))
print(minfuel)
