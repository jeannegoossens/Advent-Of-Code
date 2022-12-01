inp = open('inputs/Day12.txt').read().split('\n')

registers = {}
for l in inp:
    l = l.replace(',', '')
    instr = l.split()
    registers[instr[0]] = set(instr[2:])


def findgroupfor(reg):
    newcount = 1
    group = registers[reg]
    while newcount > 0:
        newcount = 0
        newgroup = set()
        for r in group:
            newgroup.add(r)
            for c in registers[r]:
                if c not in group:
                    newgroup.add(c)
                    newcount += 1
        group = newgroup
    return group


print("part 1", len(findgroupfor('0')))

s = set()
for re in registers.keys():
    s.add(' '.join(sorted(list(findgroupfor(re)))))

print("part 2", len(s))
