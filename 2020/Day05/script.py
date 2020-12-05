input = open('input.txt').read().split('\n')


def checkArea(rows, letter):
    if letter == 'F' or letter == 'L':
        if len(rows) > 2:
            return rows[:int(len(rows) / 2)]
        return rows[0]
    if letter == 'B' or letter == 'R':
        if len(rows) > 2:
            return rows[int(len(rows) / 2):]
        return rows[1]


def findUnoccupiedSeat(seats):
    for x in range(len(seats)):
        if seats[x] + 1 != seats[x + 1]:
            return seats[x] + 1


rows = range(128)
seats = range(8)

occupied_seats = []

for boardingpass in input:
    rows = range(128)
    seats = range(8)
    for letter in list(boardingpass)[:7]:
        rows = checkArea(rows, letter)

    for letter in list(boardingpass)[7:]:
        seats = checkArea(seats, letter)

    occupied_seats.append(rows * 8 + seats)

print('answer to part 1:', max(occupied_seats))

occupied_seats = sorted(occupied_seats)
print('answer to part 2:', findUnoccupiedSeat(occupied_seats))
