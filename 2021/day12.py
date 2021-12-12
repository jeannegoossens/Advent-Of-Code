import networkx as nx
import matplotlib.pyplot as plt  # to draw the graph

inp = [sorted(i.split('-')) for i in open('inputs/day12.txt').read().split('\n')]

G = nx.Graph()
for i in inp:
    G.add_edge(i[0], i[1])

paths = [['start']]


def check_for_unfinished_paths(paths):
    for path in paths:
        if path[-1] != 'end':
            return True
    return False


while check_for_unfinished_paths(paths):
    for path_idx in range(len(paths)):
        if path_idx < len(paths):
            path = paths[path_idx]
            if path[-1] != 'end':
                for next_node in G[path[-1]]:
                    if not next_node.islower() or (next_node.islower() and next_node not in path):
                        newpath = path.copy()
                        newpath.append(next_node)
                        paths.append(newpath)
                paths.remove(path)

print('part 1:', len(paths))


# draw the graph visually
# val_map = {'start': 1.0, 'end': 0.2}
# values = [val_map.get(node, 0.6) for node in G.nodes()]
# nx.draw(G, node_color = values, with_labels=True)
