input = open('input.txt').read().split('\n')


def runCode(input, acc):
    i = 0
    visited = []
    while i not in visited:
        visited.append(i)
        command, number = input[i].split(' ')
        if command == 'acc':
            acc += int(number)
            i += 1
        elif command == 'nop':
            i += 1
        elif command == 'jmp':
            i += int(number)
        if i >= len(input):
            return (True, acc)
    return (False, acc)


print('solution to part 1:', runCode(input, 0)[1])

for x in range(len(input)):
    acc = 0
    old = input[x]
    if input[x].split(' ')[0] == 'nop':
        input[x] = input[x].replace('nop', 'jmp')
    elif input[x].split(' ')[0] == 'jmp':
        input[x] = input[x].replace('jmp', 'nop')
    trythis = runCode(input, acc)
    if trythis[0] == True:
        print('solution to part 2:', trythis[1])
        break
    else:
        input[x] = old
