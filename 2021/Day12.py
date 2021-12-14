import networkx as nx
import matplotlib.pyplot as plt

inp = [sorted(i.split('-')) for i in open('inputs/day12.txt').read().split('\n')]

G = nx.Graph()
for i in inp:
    G.add_edge(i[0], i[1])

smallcaves = [cave for cave in G.nodes() if cave.islower()]


def check_for_unfinished_paths(paths):
    for path in paths:
        if path[-1] != 'end':
            return True
    return False


def check_node_allowed(path, node):
    if not node.islower():
        return True
    else:
        if node == 'start':
            return False

        # count how many times this new node already appears
        if path.count(node) >= 2:
            return False

        if len([cave for cave in smallcaves if path.count(cave) == 2]) > 0:
            # there already is a small cave that was visited twice
            return path.count(node) < 1
        else:
            return True


paths = [['start']]

while check_for_unfinished_paths(paths):
    for path_idx in range(len(paths)):
        if path_idx < len(paths):
            path = paths[path_idx]
            if path[-1] != 'end':
                for next_node in G[path[-1]]:
                    if check_node_allowed(path, next_node):
                        newpath = path.copy()
                        newpath.append(next_node)
                        paths.append(newpath)
                paths.remove(path)

print('part 2:', len(paths))


# draw the graph visually
# val_map = {'start': 1.0, 'end': 0.2}
# values = [val_map.get(node, 0.6) for node in G.nodes()]
# nx.draw(G, node_color = values, with_labels=True)
