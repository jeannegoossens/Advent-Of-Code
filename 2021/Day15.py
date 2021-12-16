import networkx as nx

inp = [[int(i) for i in list(x)] for x in open('inputs/day15.txt').read().split('\n')]

# skip this for part 1
newinp = [[x for x in y] for y in inp]
for y in range(len(newinp)):
    for j in range(1,5):
        newstuff = [max(1, (i+1)%10) for i in newinp[y][-len(inp[0]):]]
        newinp[y].extend(newstuff)
for j in range(1,5):
    newstuff = [[max(1, (x+1)%10) for x in y] for y in newinp[-len(inp):]]
    newinp.extend(newstuff)
inp = [[x for x in y] for y in newinp]

startnode = (0,0)
endnode = (len(inp)-1, len(inp[0])-1)

risklevels = {}
for y in range(len(inp)):
    for x in range(len(inp[0])):
        risklevels[(y,x)] = inp[y][x]

distances = {n: 1000000 for n in risklevels.keys()}
distances[startnode] = 0

# generate neighbours for each node
GG = nx.grid_graph(dim=[len(inp), len(inp[0])])

# set starting sets
unvisited = {n: 1000000 for n in risklevels.keys()}
visited = set()
currentnode = startnode

i = 1
while endnode not in visited:
    for neighbour in GG[currentnode]:
        if neighbour in unvisited:
            distance = distances[currentnode] + risklevels[neighbour]
            unvisited[neighbour] = min(distances[neighbour], distance)
            distances[neighbour] = unvisited[neighbour]
    unvisited.pop(currentnode)
    visited.update([currentnode])
    if currentnode == endnode:
        break
    currentnode = min(unvisited, key=unvisited.get)
    i += 1

print(distances[endnode])
# part 1: 373
# part 2: 2868
