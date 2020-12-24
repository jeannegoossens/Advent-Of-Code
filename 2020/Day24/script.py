input = open('input.txt').read().split('\n')

tiles = []
print(input)

for line in input:
    print(line)
    directions = {'se': line.count('se')}
    line = line.replace('se', '..')
    print(line)
    directions['nw'] = line.count('nw')
    line = line.replace('nw', '..')
    print(line)
    directions['sw'] = line.count('sw')
    line = line.replace('sw', '..')
    print(line)
    directions['ne'] = line.count('ne')
    line = line.replace('ne', '..')
    print(line)
    directions['e'] = line.count('e')
    directions['w'] = line.count('w')
    position = (abs(directions['se'] - directions['nw']), abs(directions['sw'] - directions['ne']), abs(directions['e'] - directions['w']))
    print(directions)
    if position in tiles:
        print(f'flip{position} back to white')
        tiles.pop(tiles.index(position))
    else:
        print(f'flip{position} to black')
        tiles.append(position)

print(tiles)
print(len(tiles))

# 597 too high
# 585 too high

# 367 too low
