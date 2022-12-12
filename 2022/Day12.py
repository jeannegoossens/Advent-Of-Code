inp = [[ord(char) - 96 for char in i] for i in open('inputs/Day12.txt').read().split('\n')]

Sidx = (20, 120)
Eidx = (20, 0)

inp[Sidx[0]][Sidx[1]] = 26
inp[Eidx[0]][Eidx[1]] = 1

queue = {Sidx: 0}
dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
visited = {}

loc = [k for k, v in sorted(queue.items(), key=lambda item: item[1])][0]
locdist = queue[loc]

part2found = False

while loc != Eidx:  # part 1
    loc = [k for k, v in sorted(queue.items(), key=lambda item: item[1])][0]
    locdist = queue[loc]
    del queue[loc]
    visited[loc] = locdist

    if inp[loc[0]][loc[1]] == 1 and not part2found:
        print("part 2:", locdist)
        part2found = True

    for direction in dirs:
        neighbour = (min(max(0, loc[0] + direction[0]), len(inp)-1), min(max(0, loc[1] + direction[1]), len(inp[0])-1))
        if loc != neighbour and neighbour not in visited.keys():
            if inp[loc[0]][loc[1]] - inp[neighbour[0]][neighbour[1]] <= 1:
                if neighbour not in queue.keys():
                    queue[neighbour] = locdist + 1
                else:
                    queue[neighbour] = min(locdist + 1, queue[neighbour])

print("part 1:", locdist)
