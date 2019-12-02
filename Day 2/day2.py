numbers = open('input.txt').read().split(',')
numbers = [int(i) for i in numbers]

numbers[1] = 12
numbers[2] = 2

i = 0
while numbers[i] != 99:
    if numbers[i] == 1:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] + numbers[numbers[i+2]]
    elif numbers[i] == 2:
        numbers[numbers[i+3]] = numbers[numbers[i+1]] * numbers[numbers[i+2]]
    i += 4

print(numbers[0])
