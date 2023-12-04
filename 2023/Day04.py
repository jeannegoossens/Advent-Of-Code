inp = open('inputs/Day04.txt').read().split('\n')

score = 0
cards = {i: 1 for i in range(1, 194)}

for card in inp:
    id, values = card.split(': ')
    id = int(id.split('Card ')[1])
    winning, mine = values.split(' | ')
    winning = [int(i) for i in winning.split(' ') if i.isnumeric()]
    mine = [int(i) for i in mine.split(' ') if i.isnumeric()]

    overlap = [e for e in mine if e in winning]

    # part 1
    if len(overlap) <= 2:
        score += len(overlap)
    else:
        score += 2 ** (len(overlap) - 1)

    # part 2
    for i in range(len(overlap)):
        cards[id + i + 1] += 1 * cards[id]

print(score)
print(sum(cards.values()))