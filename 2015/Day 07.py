input = open('inputs/input07.txt').read().split('\n')

wires = {}
integers = {}

for line in input:
    instr = line.split()
    if instr[-1] in wires.keys():
        raise Exception
    else:
        if (len(instr) == 3) and instr[0].isnumeric():
            integers[instr[-1]] = int(instr[0])
        wires[instr[-1]] = ' '.join(instr[:-2])

# part 2: start b with the solution to part 1
wires['b'] = '956'
integers['b'] = '956'

while len(integers.keys()) < len(wires.keys()):
    for wire, formula in wires.items():
        if wire not in integers:
            forms = formula.split()
            newformula = []
            for f in forms:
                if f in integers.keys():
                    newformula.append(str(integers[f]))
                elif f in ['NOT', 'OR', 'AND', 'LSHIFT', 'RSHIFT']:
                    if f == 'NOT':
                        newformula.append('~')
                    elif f == 'OR':
                        newformula.append('|')
                    elif f == 'AND':
                        newformula.append('&')
                    elif f == 'LSHIFT':
                        newformula.append('<<')
                    elif f == 'RSHIFT':
                        newformula.append('>>')
                else:
                    newformula.append(f)
            calculatable = True
            for n in newformula:
                if not n.lstrip('-').isnumeric() and n not in ['~', '|', '&', '<<', '>>']:
                    calculatable = False
            if wire not in integers.keys() and calculatable:
                if len(newformula) == 2:
                    wires[wire] = ~ int(newformula[1])
                elif len(newformula) == 1:
                    wires[wire] = int(newformula[0])
                else:
                    if newformula[1] == '|':
                        wires[wire] = int(newformula[0]) | int(newformula[2])
                    elif newformula[1] == '&':
                        wires[wire] = int(newformula[0]) & int(newformula[2])
                    elif newformula[1] == '<<':
                        wires[wire] = int(newformula[0]) << int(newformula[2])
                    elif newformula[1] == '>>':
                        wires[wire] = int(newformula[0]) >> int(newformula[2])
                integers[wire] = wires[wire]
            else:
                wires[wire] = ' '.join(newformula)

print(integers['a'])
