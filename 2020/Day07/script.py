input = open('input.txt').read().split('\n')

import networkx as nx
import re

DG = nx.DiGraph()

for line in input:
    line = re.split(r' bags contain | bags, | bag, | bag | bags | bags\.| bag\.', line)[:-1]
    outer = line[0]
    inner = line[1:]
    for type in inner:
        if type.strip() == 'no other':
            continue
        amount = re.findall('[0-9]+', type)[0]
        color = type[2:]
        DG.add_edge(color, outer, weight=amount)


def check(node):
    connected = [x[1] for x in DG.edges(node)]
    if len(connected) > 0:
        for n in connected:
            all_connected.append(n)
            check(n)
    return


find = 'shiny gold'
all_connected = []
check(find)
print('answer to part 1:', len(set(all_connected)))
