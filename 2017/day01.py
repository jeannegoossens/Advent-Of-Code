input = list(open('inputs/Day01.txt').read())

sum = 0
for number in range(len(input)):
    if input[number] == input[(number+1) % len(input)]:
        sum += int(input[number])

print(sum)

sum = 0
halfway = len(input) // 2
for number in range(len(input)):
    if input[number] == input[(number+halfway) % len(input)]:
        sum += int(input[number])
print(sum)