inp = [i.split('\n') for i in open('inputs/Day01.txt').read().split('\n\n')]

elves = [sum([int(i) for i in elf]) for elf in inp]

print("part 1:", max(elves))
print("part 2:", sum(sorted(elves)[-3:]))