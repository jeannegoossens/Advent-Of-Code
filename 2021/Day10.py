import statistics

inp = open("inputs/day10.txt").read().split('\n')

pairs = {'(': ')', '{': '}', '<': '>', '[': ']'}


def detect_error(line):
    opening = []
    for character in line:
        if character in pairs.keys():
            opening.append(character)
        elif character in pairs.values():
            if pairs[opening[-1]] == character:
                opening.pop(-1)
            else:
                print(f"Syntax error found on line {line} character {character} (expected {pairs[opening[-1]]}")
                return character
    if len(opening) > 0:
        print("Incomplete line {line}")
        missing = [pairs[i] for i in reversed(opening)]
        return missing


# get results for line
faults = []
missing = []
for line in inp:
    result =detect_error(line)
    if len(result) == 1:
        faults.append(result)
    else:
        missing.append(result)


# part 1 calculate score
total = 0
scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
for f in faults:
    if f:
        total += scores[f]
print('part 1:', total)


# part 2 calculate score
linescores = []
scores = {')': 1, ']': 2, '}': 3, '>': 4}
for miss in missing:
    linescore = 0
    for char in miss:
        linescore = linescore * 5 + scores[char]
    linescores.append(linescore)
print('part 2',statistics.median(linescores))