inp = open('inputs/Day16.txt').read().split(',')
print(inp)

programs = list('abcdefghijklmnop')
print(programs)

for _ in range(1_000_000_000):
    for line in inp:
        dance = line[0]
        if dance == 's':
            X = int(line[1:])
            newprograms = programs[-X:]
            newprograms.extend(programs[:-X])
            programs = newprograms
        elif dance == 'x':
            first, second = line[1:].split('/')
            temp = programs[int(first)]
            programs[int(first)] = programs[int(second)]
            programs[int(second)] = temp
        elif dance == 'p':
            first, second = line[1:].split('/')
            f = programs.index(first)
            s = programs.index(second)
            temp = programs[f]
            programs[f] = programs[s]
            programs[s] = temp

print(''.join(programs))
