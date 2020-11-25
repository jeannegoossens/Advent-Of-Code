
inp = open('input.txt').read()
image = 25*6

layers = [inp[i:i+image] for i in range(0, len(inp), image)]

least = image
for l in layers:
    if l.count('0') < least:
        least = l.count('0')

print(layers[6].count('1') * layers[6].count('2'))

# 0 = black
# 1 = white
# 2 = transparent

finalcanvas = ['0' for i in range(image)]

for l in reversed(layers):
    for i in range(image):
        if l[i] == '0':
            finalcanvas[i] = ' '
        elif l[i] == '1':
            finalcanvas[i] = 'X'

finalcanvas = ''.join(finalcanvas)
finalcanvas = [finalcanvas[i:i+25] for i in range(0, len(finalcanvas), 25)]
for f in finalcanvas:
    print(f)
