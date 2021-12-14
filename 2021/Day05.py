inp = open("inputs/day05.txt").read().split('\n')

lines = []
for i in inp:
    i = i.split(' -> ')
    x1, y1 = i[0].split(',')
    x2, y2 = i[1].split(',')
    lines.append([(int(x1), int(y1)), (int(x2), int(y2))])

# part 1 (filtering diagonal lines out)
horverlines = [l for l in lines if l[0][0] == l[1][0] or l[0][1] == l[1][1]]

points = {}

# part 1 only includes horizontal and vertical lines
for l in horverlines:
    startx = min(l[0][0], l[1][0])
    endx = max(l[0][0], l[1][0])
    starty = min(l[0][1], l[1][1])
    endy = max(l[0][1], l[1][1])

    for x in range(startx, endx + 1):
        for y in range(starty, endy + 1):
            if (x, y) in points.keys():
                points[(x, y)] += 1
            else:
                points[(x, y)] = 1

# part 2 includes diagonal lines
diaglines = [l for l in lines if l not in horverlines]
for l in diaglines:
    # first sort the start and end points by the value of x
    if l[0][0] > l[1][0]:
        l = [l[1], l[0]]

    startx = l[0][0]
    endx = l[1][0]
    starty = l[0][1]
    endy = l[1][1]

    if starty > endy:
        # if the line goes down
        for x in range(startx, endx + 1):
            if (x, starty) in points.keys():
                points[(x, starty)] += 1
            else:
                points[(x, starty)] = 1
            starty -= 1
    else:
        # if the line goes up
        for x in range(startx, endx + 1):
            if (x, starty) in points.keys():
                points[(x, starty)] += 1
            else:
                points[(x, starty)] = 1
            starty += 1

overlap = 0
for v in points.values():
    if v > 1:
        overlap += 1
print(overlap)
