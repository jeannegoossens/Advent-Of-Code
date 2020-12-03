input = open('inputs/day01.txt').read().split(', ')
print(input)

x = 0
y = 0

position = 0

visited = []

for walk in input:
    distance = int(walk[1:])

    if walk.startswith('R'):
        position += 1
        if position == 4:
            position = 0
    elif walk.startswith('L'):
        position -= 1
        if position < 0:
            position = 3

    def isVisited(x,y, visited):
        if (x,y) in visited:
            print('visited', x,y)
            return True
        else:
            return False

    if position == 0:  # north
        for i in range(distance):
            y -= 1
            if not(isVisited(x,y, visited)):
                visited.append((x,y))
            else:
                break
    elif position == 1:  # east
        for i in range(distance):
            x += 1
            if not(isVisited(x,y, visited)):
                visited.append((x,y))
            else:
                break
    elif position == 2:  # south
        for i in range(distance):
            y += 1
            if not (isVisited(x, y, visited)):
                visited.append((x, y))
            else:
                break
    elif position == 3:  #west
        for i in range(distance):
            x -= 1
            if not (isVisited(x, y, visited)):
                visited.append((x, y))
            else:
                break
    else:
        print('impossible position', walk, position)



blocks = abs(x) + abs(y)
print(blocks, x, y)

# 257 too high