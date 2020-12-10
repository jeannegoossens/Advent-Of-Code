# 2015
# Day 3

input = open('inputs/input03.txt').read().split('\n')
cos_santa = (0,0)
cos_robo = (0,0)
houses = [cos_santa]

robo = False

for x in input:
    if robo:
        cos = cos_robo
    else:
        cos = cos_santa

    if x == '>':
        cos = (cos[0]+1, cos[1])
    elif x == '<':
        cos = (cos[0]-1, cos[1])
    elif x == '^':
        cos = (cos[0], cos[1]+1)
    elif x == 'v':
        cos = (cos[0], cos[1]-1)
    houses.append(cos)

    if robo:
        cos_robo = cos
    else:
        cos_santa = cos

    robo = not(robo)

print(len(list(set(houses))))
