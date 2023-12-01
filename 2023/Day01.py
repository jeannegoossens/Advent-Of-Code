inp = [i for i in open('inputs/Day01.txt').read().split('\n')]

sum = 0

for line in inp:

    # because numbers might overlap in their final letter (e.g. twone for two and one), I want to preserve those endings
    # so that it doesn't matter in what order I do the replacements
    line = line.replace("one", 'o1e')
    line = line.replace("two", 't2o')
    line = line.replace("three", 't3e')
    line = line.replace("four", 'f4r')
    line = line.replace("five", 'f5e')
    line = line.replace("six", 's6x')
    line = line.replace("seven", 's7n')
    line = line.replace("eight", 'e8t')
    line = line.replace("nine", 'n9e')

    nr = ''
    for char in line:
        if char.isnumeric():
            nr += char
    number = ''
    number += nr[0]
    number += nr[-1]

    sum += int(number)

print(sum)
