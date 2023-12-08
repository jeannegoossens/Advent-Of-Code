import functools

inp = open('inputs/Day07.txt').read().split('\n')

# inp = """32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483""".split('\n')

what = {x.split(' ')[0]: x.split(' ')[1] for x in inp}

cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
hands = ['5ofKind', '4ofKind', 'FullHouse', '3ofKind', '2Pair', '1Pair', 'High']


def whatHand(hand):
    build = {card: hand.count(card) for card in cards}
    if 5 in build.values():
        return '5ofKind'
    elif 4 in build.values():
        return '4ofKind'
    elif 3 in build.values() and 2 in build.values():
        return 'FullHouse'
    elif 3 in build.values() and 2 not in build.values():
        return '3ofKind'
    elif list(build.values()).count(2) == 2:
        return '2Pair'
    elif list(build.values()).count(2) == 1:
        return '1Pair'
    return 'High'


def compare(item1, item2):
    for i in range(5):
        if cards.index(item1[i]) < cards.index(item2[i]):
            return -1
        elif cards.index(item1[i]) > cards.index(item2[i]):
            return 1
        else:
            return 0


camels = {hand: [] for hand in hands}
for combo in inp:
    hand, bid = combo.split(' ')
    camels[whatHand(hand)].append(hand)
allhands = []

for comb in camels.keys():
    camels[comb] = sorted(camels[comb], key = functools.cmp_to_key(compare))
    allhands.extend(camels[comb])

score = 0

allhands = list(reversed(allhands))

for i in range(len(allhands)):
    score += (i+1) * int(what[allhands[i]])

print(score)

# 253403520 too high
# 251303620 too high
# 249696880 too low
