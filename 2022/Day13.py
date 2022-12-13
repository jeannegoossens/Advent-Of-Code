import re
import ast

inp = [i.replace('\n', ',') for i in open('inputs/Day13.txt').read().split('\n\n')]

print(inp)

idxsum = 0


def compare(first, second):
    if type(first) == list and type(second) == int:
        second = [second]
    elif type(first) == int and type(second) == list:
        first = [first]

    print(first)
    print(second)

    if type(first) == int and type(second) == int:
        if first == second:
            return 2
        elif first < second:
            return True
        else:
            return False
    elif type(first) == list and type(second) == list:
        for idx, item in enumerate(first):
            if idx >= len(second):
                return False
            else:
                order = compare(item, second[idx])
                if order == 2:
                    continue
                else:
                    return order
        # if len(second) > len(first):
        return True


def checkline(line):
    mylist = ast.literal_eval(line)
    print(mylist)
    for idx in range(len(mylist)-1):
        order = compare(mylist[idx], mylist[idx+1])
        print(order)
        if order == 2:
            continue
        else:
            return order


for x in range(len(inp)):
    if inp[x] != '':
        if checkline(inp[x]):
            idxsum += x+1

print("part 1:", idxsum)
