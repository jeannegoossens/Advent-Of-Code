import re
import json

input = open('inputs/input12.txt').read()

r = list(map(int, re.findall(r'-?[0-9]+', input)))
print(sum(r))

def checkRed(dic, sum):
    if "red" in dic.keys() or "red" in dic.values():
        return sum
    else:
        for k, v in dic.items():
            if isinstance(v, dict):
                sum = checkRed(v, sum)
            elif isinstance(v, list):
                sum = checkList(v, sum)
            else:
                if isinstance(k, int):
                    sum += k
                if isinstance(v, int):
                    sum += v
        return sum

def checkList(lis, sum):
    for item in lis:
        if isinstance(item, dict):
            sum = checkRed(item, sum)
        elif isinstance(item, list):
            sum = checkList(item, sum)
        else:
            if isinstance(item, int):
                sum += int(item)
    return sum

input = json.loads(input)
print(checkRed(input, 0))
