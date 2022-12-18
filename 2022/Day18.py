inp = open('inputs/Day18.txt').read().split('\n')
inp = [[int(x) for x in i.split(',')] for i in inp]

uncovered = 0

for cube in inp:
    covered = 0
    for other in inp:
        if abs(cube[0] - other[0]) + abs(cube[1] - other[1]) + abs(cube[2] - other[2]) == 1:
            covered += 1
    uncovered += 6 - covered

print("part 1:", uncovered)
