def calc(nr):
    result = int(nr / 3) - 2
    if result <= 0:
        return 0
    return result + calc(result)


def sumup(lines):
    fuel = 0
    for line in lines:
        fuel += calc(int(line))
    return fuel


lines = open("input.txt").read().split('\n')
lines = list(filter(None, lines))

print(sumup(lines))
