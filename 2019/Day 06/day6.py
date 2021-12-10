import networkx as nx

lines = open('input.txt').read().split('\n')

# read all edges from this input
edges = []
for x in lines:
    sentence = x.split(')')
    edges.append((sentence[0], sentence[1]))
    
# create a graph and add the edges
G = nx.Graph()
G.add_edges_from(edges)

# part 1
s = 0
for n in G.nodes:
    s += len(nx.shortest_path(G, source='COM', target=n)) - 1
print(s)

# part 2
print(len(nx.shortest_path(G, source='YOU', target='SAN')) - 3)
