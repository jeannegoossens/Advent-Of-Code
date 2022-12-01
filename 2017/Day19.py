inp = open('inputs/Day19.txt').read().split('\n')

s = set([y for x in inp for y in x])
s.remove('-')
s.remove(' ')
s.remove('|')
s.remove('+')

sol = ''

row = 0
cell = inp[0].index(inp[0][-1])
direction = 'down'
d = '|'

steps = 1

while inp[row][cell] != 'T':
    if direction == 'down':
        row += 1
    elif direction == 'right':
        cell += 1
    elif direction == 'up':
        row -= 1
    elif direction == 'left':
        cell -= 1

    if inp[row][cell] in s:
        sol += inp[row][cell]
    elif inp[row][cell] == '+':
        if direction in ['up', 'down']:
            if inp[row][min(cell+1, len(inp[row])-1)] == '-':
                direction = 'right'
                d = '-'
            elif inp[row][max(0, cell-1)] == '-':
                direction = 'left'
                d = '-'
        elif direction in ['left', 'right']:
            if len(inp[min(row+1, len(inp)-1)]) >= cell:
                if inp[min(row+1, len(inp)-1)][cell] == '|':
                    direction = 'down'
                    d = '|'
                elif inp[min(row+1, len(inp)-1)][cell] == ' ':
                    if len(inp[max(0, row - 1)]) >= cell:
                        if inp[max(0, row - 1)][cell] == '|':
                            direction = 'up'
                            d = '|'
            elif len(inp[max(0, row-1)]) >= cell:
                if inp[max(0, row-1)][cell] == '|':
                    direction = 'up'
                    d = '|'
                elif inp[max(0, row-1)][cell] == ' ':
                    if len(inp[min(row + 1, len(inp) - 1)]) >= cell:
                        if inp[min(row + 1, len(inp) - 1)][cell] == '|':
                            direction = 'down'
                            d = '|'
    steps += 1

print(sol)
print(steps)
