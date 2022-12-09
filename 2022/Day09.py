inp = open('inputs/Day09.txt').read().split('\n')

dirs = {'R': (0, 1), 'U': (1, 0), 'L': (0, -1), 'D': (-1, 0)}


def run(knots):
    positions = set()
    for line in inp:
        for x in range(int(line.split()[-1])):
            # first move the head knot, since it doesn't depend on any other knot
            knots[0] = (knots[0][0] + dirs[line[0]][0], knots[0][1] + dirs[line[0]][1])
            for knot in range(1, len(knots)):
                # now for each of the other knots
                if abs(knots[knot - 1][0] - knots[knot][0]) == 2 and abs(knots[knot - 1][1] - knots[knot][1]) == 0:
                    # the knot is 2 steps removed from its predecessor in the vertical direction, and none horizontally
                    if knots[knot - 1][0] > knots[knot][0]:
                        knots[knot] = (knots[knot][0] + 1, knots[knot][1])
                    else:
                        knots[knot] = (knots[knot][0] - 1, knots[knot][1])
                elif abs(knots[knot - 1][0] - knots[knot][0]) == 0 and abs(knots[knot - 1][1] - knots[knot][1]) == 2:
                    # the knot is 2 steps removed from its predecessor in the horizontal direction, and none vertically
                    if knots[knot - 1][1] > knots[knot][1]:
                        knots[knot] = (knots[knot][0], knots[knot][1] + 1)
                    else:
                        knots[knot] = (knots[knot][0], knots[knot][1] - 1)
                elif sum(abs(a - b) for a, b in zip(knots[knot-1], knots[knot])) > 2:
                    # the knot isn't adjacent to its predecessor and isn't in the same row & column, so moves diagonally
                    if knots[knot-1][0] > knots[knot][0]:
                        knots[knot] = (knots[knot][0] + 1, knots[knot][1])
                    elif knots[knot-1][0] < knots[knot][0]:
                        knots[knot] = (knots[knot][0] - 1, knots[knot][1])
                    if knots[knot-1][1] > knots[knot][1]:
                        knots[knot] = (knots[knot][0], knots[knot][1] + 1)
                    elif knots[knot-1][1] < knots[knot][1]:
                        knots[knot] = (knots[knot][0], knots[knot][1] - 1)
            positions.add(knots[-1])
    return len(positions)


# part 1
knots = [(0, 0), (0, 0)]
print("Part 1:", run(knots))

# part 2
knots = [(0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0), (0, 0)]
print("Part 2:", run(knots))
