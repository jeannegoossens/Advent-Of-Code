lines = open("input.txt").read().split('\n')
lines = list(filter(None, lines))

lst = []

for x in lines:
    line = x.split()
    inpt = {
        'id': line[0][1:],
        'fromleft': int(line[2].split(',')[0]),
        'fromtop': int(line[2].split(',')[1][:-1]),
        'width': int(line[3].split('x')[0]),
        'height': int(line[3].split('x')[1])
    }
    lst.append(inpt)

fabric = [['.']*2000 for i in range(2000)]

for y in lst:
    for i in range(y['fromtop'], (y['fromtop'] + y['height'])):
        for j in range(y['fromleft'], (y['fromleft'] + y['width'])):
            if fabric[i][j] == '.':
                fabric[i][j] = y['id']
            else:
                fabric[i][j] = 'X'

counter = 0
for a in fabric:
    for b in a:
        if b == 'X':
            counter += 1

print(counter)

for k in reversed(lst):
    overlap = False
    for u in range(k['fromtop'], (k['fromtop'] + k['height'])):
        for e in range(k['fromleft'], (k['fromleft'] + k['width'])):
            if (fabric[u][e] == 'X'):
                overlap = True
    if (overlap == False):
        print(k)