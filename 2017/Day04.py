input = open('inputs/Day04.txt').read().split('\n')

pt1 = 0
pt2 = 0
for line in input:
    if len(line.split()) == len(set(line.split())):
        pt1 += 1
    l = [''.join(sorted([j for j in i])) for i in line.split()]
    if len(l) == len(set(l)):
        pt2 += 1

print(pt1)
print(pt2)

