inp = open('inputs/Day03.txt').read().split('\n')

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

# part 1
priosum = 0

for line in inp:
    half = len(line) // 2
    first = line[:half]
    second = line[half:]
    a = list(set(first) & set(second))
    priosum += letters.index(a[0]) + 1
print("part 1:", priosum)

# [art 2
i = 0
groupsum = 0

while i < (len(inp) - 2):
    a = list(set(inp[i]) & set(inp[i+1]) & set(inp[i+2]))
    groupsum += letters.index(a[0]) + 1
    i += 3

print("part 2:", groupsum)
