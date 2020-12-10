# 2015
# Day 5

input = open('inputs/input05.txt').read().split('\n')

def threeVowels(input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for x in input:
        if x in vowels:
            count += 1
    if count >= 3:
        return True
    else:
        return False

def doubleLetter(input):
    for x in range(len(input)):
        try:
            if input[x] == input[x+1]:
                return True
        except IndexError:
            return False

def forbiddenStrings(input):
    if 'ab' in input or 'cd' in input or 'pq' in input or 'xy' in input:
        return False
    else:
        return True

def doublePair(input):
    x = 0
    y = 2
    while y < len(input):
        if input[x:y] in input[y:]:
            return True
        else:
            x += 1
            y += 1
    return False

def skipOne(input):
    for x in range(len(input)):
        try:
            if input[x] == input[x+2]:
                return True
        except IndexError:
            return False

def isNice(input):
    # if threeVowels(input) and doubleLetter(input) and forbiddenStrings(input):
    #     return 1
    # else:
    #     return 0
    if doublePair(input) and skipOne(input):
        return 1
    else:
        return 0

allnice = 0
for x in input:
    allnice += isNice(x)

print(allnice)