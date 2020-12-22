input = open('input.txt').read().split('\n\n')

p1 = list(map(int, input[0].split('\n')[1:]))
p2 = list(map(int, input[1].split('\n')[1:]))

print(p1)
print(p2)


def score(cards):
    score = 0
    cards = list(reversed(cards))
    for x in range(0, len(cards)):
        score += (x+1) * cards[x]
    return score


def playGame(p1, p2):
    round = 1
    while len(p1) != 0 and len(p2) != 0:
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)

        if p1_card > p2_card:
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)

        round += 1

    if len(p1) > len(p2):
        return '1', score(p1)
    else:
        return '2', score(p2)


winner, points = playGame(p1, p2)

print('\nSolution to part 1:', points, '(player', winner, 'won)')
