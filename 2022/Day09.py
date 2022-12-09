inp = open('inputs/Day09.txt').read().split('\n')

positions = [(0,0)]
head = (0,0)
tail = (0,0)

dirs = {'R': (0, 1), 'U': (1, 0), 'L': (0, -1), 'D': (-1, 0)}

for line in inp:
    for x in range(int(line.split()[-1])):
        head = (head[0] + dirs[line[0]][0], head[1] + dirs[line[0]][1])
        manhattan = sum(abs(a - b) for a, b in zip(head, tail))
        if manhattan == 2 and ((abs(head[0] - tail[0]) == 2 and abs(head[1] - tail[1]) == 0)
                or (abs(head[1] - tail[1]) == 2 and abs(head[0] - tail[0]) == 0)):
            tail = (tail[0] + dirs[line[0]][0], tail[1] + dirs[line[0]][1])
        elif manhattan > 2:
            if head[0] > tail[0]:
                tail = (tail[0]+1, tail[1])
            elif head[0] < tail[0]:
                tail = (tail[0]-1, tail[1])
            if head[1] > tail[1]:
                tail = (tail[0], tail[1]+1)
            elif head[1] < tail[1]:
                tail = (tail[0], tail[1]-1)
        positions.append(tail)

print(len(set(positions)))