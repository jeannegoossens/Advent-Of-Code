# 2015
# Day 9

input = open('inputs/input09.txt').read()

import networkx as nx
from itertools import permutations

G = nx.Graph()
for x in input.split('\n'):
    y = x.split(' ')
    G.add_edge(y[0], y[2], weight=int(y[4]))

print(G.edges.data('weight'))
maxdistance = 0

for x in permutations(G.nodes()):
    distance = 0
    prev = x[0]
    for node in x[1:]:
        distance += G[prev][node]['weight']
        prev = node
    maxdistance = max(maxdistance, distance)

print(maxdistance)