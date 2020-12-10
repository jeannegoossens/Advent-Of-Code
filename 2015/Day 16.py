input = open('inputs/input16.txt').read().split('\n')

gift = {'children': 3, 'cats': 7, 'samoyeds': 2, 'pomeranians': 3, 'akitas': 0, 'vizslas': 0, 'goldfish': 5, 'trees': 3, 'cars': 2, 'perfumes': 1}

sues = {}

for sue in input:
    sue = sue.replace(',', '').replace(':', '').split(' ')
    character = {}
    for info in range(2, len(sue), 2):
        character[sue[info]] = int(sue[info+1])
    sues[sue[1]] = character


def checkSue(character, gift):
    for k, v in character.items():
        if k in ['cats', 'trees']:
            if v <= gift[k]:
                return False
        elif k in ['pomeranians', 'goldfish']:
            if v >= gift[k]:
                return False
        elif v != gift[k]:
            return False
    return True


for sue, chars in sues.items():
    if checkSue(chars, gift):
        print('FOUND', sue)
        break
