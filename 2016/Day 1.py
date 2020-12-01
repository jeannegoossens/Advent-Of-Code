input = """L5, R1, R3, L4, R3, R1, L3, L2, R3, L5, L1, L2, R5, L1, R5, R1, L4, R1, R3, L4, L1, R2, R5, R3, R1, R1, L1, R1, L1, L2, L1, R2, L5, L188, L4, R1, R4, L3, R47, R1, L1, R77, R5, L2, R1, L2, R4, L5, L1, R3, R187, L4, L3, L3, R2, L3, L5, L4, L4, R1, R5, L4, L3, L3, L3, L2, L5, R1, L2, R5, L3, L4, R4, L5, R3, R4, L2, L1, L4, R1, L3, R1, R3, L2, R1, R4, R5, L3, R5, R3, L3, R4, L2, L5, L1, L1, R3, R1, L4, R3, R3, L2, R5, R4, R1, R3, L4, R3, R3, L2, L4, L5, R1, L4, L5, R4, L2, L1, L3, L3, L5, R3, L4, L3, R5, R4, R2, L4, R2, R3, L3, R4, L1, L3, R2, R1, R5, L4, L5, L5, R4, L5, L2, L4, R4, R4, R1, L3, L2, L4, R3"""
# input = """R8, R4, R4, R8"""
input = input.split(', ')
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