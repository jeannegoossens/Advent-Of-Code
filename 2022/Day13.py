import ast

inp = [ast.literal_eval(i.replace('\n', ',')) for i in open('inputs/Day13.txt').read().split('\n\n')]

idxsum = 0


def compare(first, second, level=0):
    if type(first) == int and type(second) == list:
        return compare([first], second, level)
    elif type(first) == list and type(second) == int:
        return compare(first, [second], level)

    if type(first) == list and type(second) == list:
        for x in range(max(len(first), len(second))):
            if x >= len(first):
                return 1
            elif x >= len(second):
                return -1
            else:
                comparison = compare(first[x], second[x], level+1)
                if comparison == 1 or comparison == -1:
                    return comparison
                else:
                    continue

    elif type(first) == int and type(second) == int:
        if first < second:
            return 1
        elif first > second:
            return -1
        elif first == second:
            return 0

    return 0


for line in range(len(inp)):
    if compare(inp[line][0], inp[line][1]) == 1:
        idxsum += line+1
print("part 1:", idxsum)


inp = [ast.literal_eval(i) for i in open('inputs/Day13.txt').read().split('\n') if i != '']
inp.append([[6]])
inp.append([[2]])


def bubblesort(inp):
    offset = 1
    changed = True
    while changed:
        changed = False
        for i in range(len(inp) - offset):
            if compare(inp[i], inp[i + 1]) < 1:
                inp[i], inp[i + 1] = inp[i + 1], inp[i]
                changed = True
        offset += 1
    return inp


inp = bubblesort(inp)
print("part 2:", (inp.index([[2]])+1) * (inp.index([[6]])+1))
