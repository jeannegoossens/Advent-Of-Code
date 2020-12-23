test = "389125467"
labelling = "916438275"

cups = list(map(int, list(test)))


def find_destination(cups, current):
    d = cups[current] - 1
    while True:
        for x in cups:
            if x == d:
                return cups.index(d)
        d -= 1
        if d < min(cups):
            d = max(cups)


def move(cups, current):
    pick = [x % len(cups) for x in range(current+1, current+4)]
    print('pick', pick)

    pick = [cups[x] for x in pick]
    current_number = cups[current]

    print('current:', cups[current])
    print('cups:', cups)
    print('pick:', pick)

    del cups[current+1:current+4]
    destination = find_destination(cups, current)

    print('cups:', cups)
    print('destination:', cups[destination])

    cups.insert(destination+1, pick[0])
    cups.insert(destination+2, pick[1])
    cups.insert(destination+3, pick[2])

    print('cups:', cups)

    next = cups.index(current_number)+1

    return next, cups


next = 0
for i in range(10):
    print('\n-- move', i+1, '--')
    next, cups = move(cups, next)