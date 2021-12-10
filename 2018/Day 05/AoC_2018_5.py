lines = open("input.txt").read()


def reactpolymer(lns):
    finished = False
    while not finished:
        for x in range(0, len(lns)):
            if x == (len(lns) - 1):
                finished = True
                break
            if lns[x].lower() == lns[x + 1].lower():
                if not((lns[x].isupper() and lns[x + 1].isupper()) or (lns[x].islower() and lns[x + 1].islower())):
                    lns = lns[:x] + lns[x + 2:]
                    break
    return len(lns)


def removeletter(lns):
    bestlength = len(lns)
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        lnscopy = lns.replace(letter, '').replace(letter.upper(), '')
        bestlength = min(bestlength, reactpolymer(lnscopy))
    return bestlength


print(removeletter(lines))
