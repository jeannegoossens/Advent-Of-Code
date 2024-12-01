inp = [[int(i.split("   ")[0]), int(i.split("   ")[1])] for i in open('inputs/Day01.txt').read().split('\n')]

left = sorted([i[0] for i in inp])
right = sorted([i[1] for i in inp])

distance = 0
similarity = 0

for idx, number in enumerate(left):
    distance += abs(number - right[idx])
    similarity += number * right.count(number)

print("Part 1: ", distance)
print("Part 2: ", similarity)
