import networkx as nx

# read the input
lines = open("input.txt").read().split('\n')
lines = list(filter(None, lines))

# read all edges from this input
edges = []
for x in lines:
    sentence = x.split()
    edges.append((sentence[1], sentence[7]))

# created a directed graph and add the edges
DG = nx.DiGraph()
DG.add_edges_from(edges)

# print the solution to this challenge
# nx.topological_sort() would give an answer
# but it would not sort alphabetically when multiple nodes are available
# nx.lexicographical_topological_sort does the trick
print(''.join(nx.lexicographical_topological_sort(DG)))

# challenge part 2
for node in DG.nodes:
    DG.nodes[node]['work'] = 61 + ord(node) - ord('A')

workers = 5

time = 0
while DG.nodes:
    available = [node for node in DG.nodes if DG.in_degree(node) == 0]
    available.sort()

    for worker, node in zip(range(workers), available):
        print("%s: worker %s is on task %s" % (time, worker, node))
        DG.nodes[node]['work'] -= 1

        if DG.nodes[node]['work'] == 0:
            DG.remove_node(node)
    time += 1

print("finised at %s" % time)