# extra code to explore the networkx package a bit

import networkx as nx

lines = open("input.txt").read().split('\n')
lines = list(filter(None, lines))

edges = []
for x in lines:
    sentence = x.split()
    pair = (sentence[1], sentence[7])
    edges.append(pair)

print(edges)

DG = nx.DiGraph()
DG.add_edges_from(edges)

# print some interesting stuff
print(DG.number_of_nodes())
print(DG.number_of_edges())
print(DG.degree)

# can also print related nodes for each node
print(list(DG.successors('A')))
print(list(DG.successors('C')))
print(list(DG.neighbors('A')))

# show the shortest path between each pair of nodes
print(dict(nx.all_pairs_shortest_path(DG)))

# print the correct order of nodes for this exercise
print(''.join(nx.lexicographical_topological_sort(DG)))

# visualize this graph
import matplotlib.pyplot as plt
nx.draw(DG, with_labels=True)
plt.show()
