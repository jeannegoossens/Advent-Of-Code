# 2015
# Day 1

input = open('inputs/input01.txt').read()
floor = 0
count = 0

for x in input:
    count += 1
    if x == '(':
        floor += 1
    elif x == ')':
        floor -= 1

    # for part 2
    if floor < 0:
        print('basement reached', count, floor)
        break

print(floor)