lines = open("input.txt").read().split('\n')
lines = list(filter(None, lines))

def findChecksum(lines):
    twice = 0
    thrice = 0
    for x in lines:
        letters = []
        for y in x:
            if (x.count(y) > 1):
                letters.append(x.count(y))
        if (2 in letters):
            twice += 1
        if (3 in letters):
            thrice += 1
    return (twice*thrice)

def findSimilar(lines):
    for x in lines:
        for y in lines:
            diffs = [i for i in range(len(x)) if x[i] != y[i]]
            if (len(diffs) == 1):
                print(x)
                print(y)
                # TODO print string without differing character
                return

findSimilar(lines)