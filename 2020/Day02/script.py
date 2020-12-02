input = open('input.txt').read().split('\n')

correct_first = 0
correct_second = 0

for line in input:
    rule, letter, password = line.replace(':', '').split(' ')
    least, most = map(int, rule.split('-'))

    # for part 1: count the occurrence of the letter in the password
    # count should be between (including) boundaries
    if least <= password.count(letter) <= most:
        correct_first += 1

    # for part 2: count only the occurrence of the letter in the given indices
    # count should be exactly 1
    password = password[least - 1] + password[most - 1]
    if password.count(letter) == 1:
        correct_second += 1

print('answer to part 1:', correct_first)
print('answer to part 2:', correct_second)
