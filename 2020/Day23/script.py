inp = '916438275'
testinp = '389125467'


# PART 1 STRING METHOD

def rearrange(cups, number):
    cups = number + cups.split(number)[1] + cups.split(number)[0]
    return cups


current = 0
cups = inp
for i in range(100):
    currentcup = cups[0]

    # pick up 3 cups
    clockwise = cups[1:4]
    cups = cups.replace(clockwise, '')
    nextcup = cups[1]

    # find the destination cup
    destination = (int(currentcup) - 1) % 9
    if destination == 0:
        destination = 9
    while str(destination) in clockwise:
        destination = (destination - 1) % 9
        if destination == 0:
            destination = 9

    # replace the three cups
    cups = rearrange(cups, nextcup)
    cups = cups.replace(str(destination), str(destination) + clockwise)

print('part 1:', rearrange(cups, '1')[1:])
