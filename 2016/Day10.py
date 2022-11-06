inp = [i for i in open("inputs/day10.txt").read().split('\n')]

bots = {}
outputs = {}
foundhim = False

for line in inp:
    instructions = line.split()
    if instructions[0] == 'value':
        if instructions[5] in bots.keys():
            if len(bots[instructions[5]]) < 2:
                bots[instructions[5]].append(int(instructions[1]))
        else:
            bots[instructions[5]] = [int(instructions[1])]


while len(inp) > 0:
    newinp = []
    for line in inp:
        instructions = line.split()
        if instructions[0] == 'bot':
            if instructions[1] in bots.keys() and len(bots[instructions[1]]) == 2:
                frombot = instructions[1]
                if sorted(bots[frombot])[0] == 17 and sorted(bots[frombot])[1] == 61:
                    foundhim = True
                    print("part 1:", frombot)
                low = instructions[6]
                high = instructions[11]
                if instructions[5] == 'bot':
                    if low in bots.keys():
                        bots[low].append(sorted(bots[frombot])[0])
                    else:
                        bots[low] = [sorted(bots[frombot])[0]]
                elif instructions[5] == 'output':
                    if low == 0 or low == 1 or low == 2:
                        print('low', low, sorted(bots[frombot]))
                    if low in outputs.keys():
                        outputs[low].append(sorted(bots[frombot])[0])
                    else:
                        outputs[low] = [sorted(bots[frombot])[0]]
                if instructions[10] == 'bot':
                    if high in bots.keys():
                        bots[high].append(sorted(bots[frombot])[1])
                    else:
                        bots[high] = [sorted(bots[frombot])[1]]
                elif instructions[10] == 'output':
                    if high == 0 or high == 1 or high == 2:
                        print('high', high, sorted(bots[frombot]))
                    if high in outputs.keys():
                        outputs[high].append(sorted(bots[frombot])[1])
                    else:
                        outputs[high] = [sorted(bots[frombot])[1]]
                bots.pop(frombot)
            else:
                newinp.append(line)
    inp = newinp

print("part 2:", outputs['0'][0]*outputs['1'][0]*outputs['2'][0])
