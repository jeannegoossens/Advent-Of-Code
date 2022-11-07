inp = open('inputs/Day07.txt').read().split('\n')

names = {}
supporting = set()
nested = set()

for line in inp:
    line = line.replace(',', '')
    tower = line.split()
    names[tower[0]] = tower[1].lstrip('(').rstrip(')')
    if len(tower) > 2:
        for x in tower[3:]:
            nested.add(x)
        supporting.add(tower[0])

print(supporting - nested)
print(names)
