
inp = open('input.txt').read()
image = 25*6

layers = [inp[i:i+image] for i in range(0, len(inp), image)]

least = image
for l in layers:
    if l.count('0') < least:
        least = l.count('0')
        print(layers.index(l))

print(layers[6].count('1') * layers[6].count('2'))
