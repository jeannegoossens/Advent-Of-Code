# 2015
# Day 6

import re

input = open('inputs/input06.txt').read().split('\n')

grid = [[0 for i in range(1000)] for j in range(1000)]


def through(numbers):
    cos = []
    for a in range(numbers[0], numbers[2]+1):
        for b in range(numbers[1], numbers[3]+1):
            cos.append((a,b))
    return cos

def flip(cos, grid, setting):
    for c in cos:
        if setting == 'on':
            grid[c[0]][c[1]] += 1
        elif setting == 'off':
            grid[c[0]][c[1]] = max(0, grid[c[0]][c[1]]-1)
        elif setting == 'toggle':
            grid[c[0]][c[1]] += 2  # part 2
            # if grid[c[0]][c[1]] == 1:
            #     grid[c[0]][c[1]] = 0
            # else:
            #     grid[c[0]][c[1]] = 1

    return grid

for x in input:
    numbers = list(map(int, re.findall(r'[0-9]+', x)))
    cos = through(numbers)
    if x.startswith('turn on'):
        setting = 'on'
    elif x.startswith('turn off'):
        setting = 'off'
    else:
        setting = 'toggle'
    grid = flip(cos, grid, setting)

print(sum(sum(x) for x in grid))