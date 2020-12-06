input = list(open('inputs/day1.txt').read())

sum = 0
for number in range(len(input)):
    if input[number] == input[(number+1) % len(input)]:
        sum += int(input[number])

print(sum)