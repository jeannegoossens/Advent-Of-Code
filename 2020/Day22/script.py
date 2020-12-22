input = open('inp.txt').read().split('\n\n')

deck1 = list(map(int, input[0].split('\n')[1:]))
deck2 = list(map(int, input[1].split('\n')[1:]))


def score(cards):
    score = 0
    cards = list(reversed(cards))
    for x in range(0, len(cards)):
        score += (x+1) * cards[x]
    return score


def playGame(p1, p2):
    past_decks = [{'p1': p1.copy(), 'p2': p2.copy()}]
    while len(p1) != 0 and len(p2) != 0:
        p1_card = p1.pop(0)
        p2_card = p2.pop(0)

        if len(p1) >= p1_card and len(p2) >= p2_card:
            winner, points = playGame(p1[0:p1_card].copy(), p2[0:p2_card].copy())
        else:
            if p1_card > p2_card:
                winner = '1'
            else:
                winner = '2'

        if winner == '1':
            p1.append(p1_card)
            p1.append(p2_card)
        else:
            p2.append(p2_card)
            p2.append(p1_card)

        deck = {'p1': p1.copy(), 'p2': p2.copy()}
        if deck in past_decks:
            return '1', score(p1)
        past_decks.append(deck)

    if len(p1) > len(p2):
        return '1', score(p1)
    else:
        return '2', score(p2)


winner, points = playGame(deck1, deck2)

print('Solution to part 2:', points, '(player', winner, 'won)')
