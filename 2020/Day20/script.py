input = open('input.txt').read()[:-1].split('\n\n')

tiles = {}
for tile in input:
    lines = tile.split('\n')
    tileid = int(lines[0][5:-1])
    tile = lines[1:]
    tiles[tileid] = {
        'tile': tile,
        'north': tile[0],
        'south': tile[-1],
        'west': ''.join([x[0] for x in tile]),
        'east': ''.join([x[-1] for x in tile])
    }


for id, tile in tiles.items():
    valid = []
    for sid, second in tiles.items():
        if id != sid:
            for c in [second['north'], reversed(second['north']),
                      second['south'], reversed(second['south']),
                      second['west'], reversed(second['west']),
                      second['east'], reversed(second['east'])]:
                if tile['north'] == c:
                    valid.append('north')
                if tile['south'] == c:
                    valid.append('south')
                if tile['west'] == c:
                    valid.append('west')
                if tile['east'] == c:
                    valid.append('east')
    print(id, set(valid))