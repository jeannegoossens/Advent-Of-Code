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

# load the graph
values = {}
for y in range(len(inp)):
    for x in range(len(inp[0])):
        values[(y,x)] = inp[y][x]

GG = nx.grid_graph(dim=[len(inp), len(inp[0])])
nx.set_node_attributes(GG, values, "risklevel")


# start Dijkstra
def getweight(u, v, d):
    node_v_wt = GG.nodes[v]["risklevel"]
    return node_v_wt


shortest = nx.dijkstra_path(GG, (0,0), (len(inp)-1, len(inp[0])-1), weight=getweight)
total = 0
for node in shortest:
    total += GG.nodes[node]['risklevel']
print(total-inp[0][0])

# part 1: 373
# part 2: 2868
