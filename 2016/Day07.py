import re
inp = [i for i in open("inputs/day07.txt").read().split('\n')]


def detectABBA(chars):
    if chars[0] != chars[1] and chars[0] == chars[3] and chars[1] == chars[2]:
        return True
    return False


def checkABBA(line):
    inside = list(re.findall(r"\[(\b[a-z]+\b)\]", line))
    outside = re.sub(r"(\[\b[a-z]+\b\])", '-', line).split('-')
    for inner in inside:
        for c in range(len(inner[:-3])):
            if detectABBA(inner[c:c+4]):
                return 0
    for outer in outside:
        for c in range(len(outer[:-3])):
            if detectABBA(outer[c:c+4]):
                return 1
    return 0


def detectABA(sequence):
    return sequence[0] == sequence[2] and sequence[0] != sequence[1]


def detectBAB(aba, sequence):
    return sequence == aba[1]+aba[0]+aba[1]


def checkABA(line):
    inside = list(re.findall(r"\[(\b[a-z]+\b)\]", line))
    outside = re.sub(r"(\[\b[a-z]+\b\])", '-', line).split('-')
    ABAs = []
    for outer in outside:
        for c in range(len(outer[:-2])):
            if detectABA(outer[c:c+3]):
                ABAs.append(outer[c:c+3])
    for inner in inside:
        for c in range(len(inner[:-2])):
            for aba in ABAs:
                if detectBAB(aba, inner[c:c+3]):
                    return 1
    return 0


countABBA = 0
countABA = 0
for line in inp:
    countABBA += checkABBA(line)
    countABA += checkABA(line)

print("part 1:", countABBA)
print("part 2:", countABA)
