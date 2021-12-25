# inp = open('inputs/day25.txt').read().split('\n')
inp = open('input.txt').read().split('\n')

east_cucumbers = set()
south_cucumbers = set()

boardwidth = len(inp[0])
boardheight = len(inp)

for y in range(len(inp)):
    for x in range(len(inp[0])):
        if inp[y][x] == '>':
            east_cucumbers.add((y,x))
        elif inp[y][x] == 'v':
            south_cucumbers.add((y,x))

print(sorted(east_cucumbers))
print(sorted(south_cucumbers))

def generation(east, south):
    # move east facing sea cucumbers
    east_movers = set()
    for cucumber in east:
        if (cucumber[0], (cucumber[1]+1)%boardwidth) not in east and (cucumber[0], (cucumber[1]+1)%boardwidth) not in south:
            east_movers.add(cucumber)
    for cucumber in east_movers:
        east.remove(cucumber)
        east.add((cucumber[0], (cucumber[1]+1)%boardwidth))
    
    # move south facing sea cucumbers
    south_movers = set()
    for cucumber in south:
        if ((cucumber[0]+1)%boardheight, cucumber[1]) not in east and ((cucumber[0]+1)%boardheight, cucumber[1]) not in south:
            south_movers.add(cucumber)
    if len(east_movers) + len(south_movers) == 0:
        return False, False
    for cucumber in south_movers:
        south.remove(cucumber)
        south.add(((cucumber[0]+1)%boardheight, cucumber[1]))
    return east, south


# print(east_cucumbers, "\n", south_cucumbers)
step = 0

while east_cucumbers != False and south_cucumbers != False:
    east_cucumbers, south_cucumbers = generation(east_cucumbers, south_cucumbers)
    step += 1

print(step)
