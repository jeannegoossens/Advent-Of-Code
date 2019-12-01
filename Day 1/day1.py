def calc(nr):
    result = int(nr / 3) - 2
    if result <= 0:
        return 0
    return result + calc(result)


def sumup():
    lines = open("input.txt").read().split('\n')
    lines = list(filter(None, lines))
    sum = 0
    for line in lines:
        sum += calc(int(line))
    return sum


print(sumup())
# 5068326 is too low
