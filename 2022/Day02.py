inp = [i.split() for i in open('inputs/Day02.txt').read().split('\n')]

them = ['A', 'B', 'C']
me = ['X', 'Y', 'Z']

totalscore_1 = 0
totalscore_2 = 0

for match in inp:
    # part 1
    if me.index(match[1]) == them.index(match[0]):
        totalscore_1 += 3 + me.index(match[1]) + 1
    elif (me.index(match[1]) + 1) % 3 == them.index(match[0]):
        totalscore_1 += 0 + me.index(match[1]) + 1
    else:
        totalscore_1 += 6 + me.index(match[1]) + 1

    # part 2
    if match[1] == 'X':  # loss
        totalscore_2 += 0 + me.index(me[them.index(match[0]) - 1]) + 1
    elif match[1] == 'Y':  # draw
        totalscore_2 += 3 + them.index(match[0]) + 1
    else:  # win
        totalscore_2 += 6 + me.index(me[(them.index(match[0]) + 1) % 3]) + 1

print(totalscore_1)
print(totalscore_2)
