algorithm, image = open('inputs/day20.txt').read().split('\n\n')
# algorithm, image = open('testinput.txt').read().split('\n\n')

image = [list(i) for i in image.split('\n')]
pixels = set()
for y in range(len(image)):
    for x in range(len(image[0])):
        if image[y][x] == '#':
            pixels.update([(y,x)])

neighbours = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1), ( 0, 0), ( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)]


def findbounds(image):
    miny = min([pixel[0] for pixel in image])
    maxy = max([pixel[0] for pixel in image])
    minx = min([pixel[1] for pixel in image])
    maxx = max([pixel[1] for pixel in image])
    return [(miny, minx), (maxy, maxx)]


def printimage(image):
    bounds = findbounds(image)
    for y in range(bounds[0][0], bounds[1][0]+1):
        row = ''
        for x in range(bounds[0][1], bounds[1][1]+1):
            if (y,x) in image:
                row += '#'
            else:
                row += '.'
        print(row)


def enhance_image(pixels, bounds, background):
    newimage = set()
    boundary = {  # get all pixels in the actual image
        (x, y)
        for x in range(bounds[0][1], bounds[1][1] + 1)
        for y in range(bounds[0][0], bounds[1][0] + 1)
    }
    for y in range(bounds[0][0] - 1, bounds[1][0] + 2):
        for x in range(bounds[0][1] - 1, bounds[1][1] + 2):
            countneighbours = ''
            for neighbour in neighbours:
                if background:
                    if (y+neighbour[0], x+neighbour[1]) in pixels or (y+neighbour[0], x+neighbour[1]) not in boundary:
                        countneighbours += '1'
                    else:
                        countneighbours += '0'
                else:
                    if (y+neighbour[0], x+neighbour[1]) in pixels:
                        countneighbours += '1'
                    else:
                        countneighbours += '0'
            if algorithm[int(countneighbours, 2)] == '#':
                newimage.update([(y,x)])
    return newimage


def countlit(image):
    return len(image)


bounds = findbounds(pixels)
for step in range(50):
    background = step % 2 == 1

    # expand the bounds by 1 in all directions each step
    bounds = [(bounds[0][0] - 1, bounds[0][1] - 1), (bounds[1][0] + 1, bounds[1][1] + 1)]

    pixels = enhance_image(pixels, bounds, background)

    if step == 1:
        print("part 1:", countlit(pixels))
    elif step == 49:
        print("part 2:", countlit(pixels))

# part 1: 5179
# part 2: 16112
