input = open('inputs/input02.txt').read().split('\n')
paper = 0
ribbon = 0

for x in input:
    l,w,h = map(int, x.split('x'))
    slack = sorted([l,w,h])[0] * sorted([l,w,h])[1]
    surface = 2 * l * w + 2 * w * h + 2 * h * l
    paper += slack + surface
    ribbon += sorted([l,w,h])[0]*2 + sorted([l,w,h])[1]*2 + l*w*h

print(paper)
print(ribbon)
