inp = [[int(i) for i in list(x)] for x in open("inputs/day9.txt").read().split('\n')]
# inp = [[int(i) for i in list(x)] for x in open("testinput.txt").read().split('\n')]
print(inp)

generalneighbours = [(-1, 0), (0, -1), (1, 0), (0, 1)]

sum = 0

for y in range(len(inp)):
    for x in range(len(inp[0])):
        totalneighbours = 0
        neighbours = generalneighbours.copy()
        if y == 0:
            neighbours.remove((-1,0))
        if y == len(inp)-1:
            neighbours.remove((1,0))
        if x == 0:
            neighbours.remove((0,-1))
        if x == len(inp[0])-1:
            neighbours.remove((0,1))
        for n in neighbours:
            if inp[y+n[0]][x+n[1]] > inp[y][x]:
                totalneighbours += 1
        if len(neighbours) == totalneighbours:
            sum += 1 + inp[y][x]
print(sum)