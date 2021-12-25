# inp = open('inputs/day25.txt').read().split('\n')
inp = open('testinput.txt').read().split('\n')

east_cucumbers = set()
south_cucumbers = set()

boardwidth = len(inp[0])
boardheight = len(inp)

for y in range(len(inp)):
    for x in range(len(inp)):
        if inp[y][x] == '>':
            east_cucumbers.add((y,x))
        elif inp[y][x] == 'v':
            south_cucumbers.add((y,x))


def generation(east, south):
    east_movers = set()
    for cucumber in east:
        if (cucumber[0], (cucumber[1]+1)%boardwidth) not in east and (cucumber[0], (cucumber[1]+1)%boardwidth) not in south:
            east_movers.add(cucumber)
    for cucumber in east:
        if cucumber in east_movers:
            east.remove(cucumber)
            east.add((cucumber[0], (cucumber[1]+1)%boardwidth))
    south_movers = set()
    for cucumber in south:
        if (cucumber[0], (cucumber[1]+1)%boardwidth) not in east and (cucumber[0], (cucumber[1]+1)%boardwidth) not in south:
            south_movers.add(cucumber)
    if len(east_movers) + len(south_movers) == 0:
        return False, False
    for cucumber in south_movers:
        south.remove(cucumber)
        south.add(((cucumber[0]+1)%boardheight, cucumber[1]))
    return east, south


step = 0
while east_cucumbers and south_cucumbers:
    east_cucumbers, south_cucumbers = generation(east_cucumbers, south_cucumbers)
    step += 1
    print(step)

print(step)
