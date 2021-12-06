fish = [int(i) for i in open("inputs/day6.txt").read().split(',')]


def runday(fish):
    newday = []
    for f in fish:
        if f > 0:
            newday.append(f-1)
        elif f == 0:
            newday.append(6)
            newday.append(8)
    return newday


for i in range(80):
    fish = runday(fish)
print('part 1', len(fish))
