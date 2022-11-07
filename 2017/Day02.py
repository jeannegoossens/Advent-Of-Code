input = [[int(f) for f in i.split('\t')] for i in open('inputs/Day02.txt').read().split('\n')]


checksum = 0
second = 0
for line in input:
    checksum += abs(max(line) - min(line))
    for i in line:
        for j in line:
            if j != i:
                if i % j == 0:
                    second += i // j

print(checksum)
print(second)
