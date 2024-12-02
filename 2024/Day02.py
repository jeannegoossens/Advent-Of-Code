inp = [[int(x) for x in i.split()] for i in open('inputs/Day02.txt').read().split('\n')]


def check_safe(report):
    increase = report[0] < report[1]
    last = report[0]
    safe = True

    for level in report[1:]:
        if level == last:
            safe = False
        if abs(level - last) > 3 or abs(level - last) < 1:
            safe = False
        if (last < level) != increase:
            safe = False
        last = level

    return safe


def check_safe_dampened(report):
    allowance = 0
    for i in range(len(report)):
        without = report.copy()
        without.pop(i)
        allowance += check_safe(without)
    if allowance == 0:
        return False
    return True


countSafe = 0
countSafeDampened = 0

for report in inp:
    countSafe += check_safe(report)
    countSafeDampened += check_safe_dampened(report)

print("Part 1:", countSafe)
print("Part 2:", countSafeDampened)
