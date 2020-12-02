input = open('input.txt').read().split('\n')


def checkPassword(line):
    rule, letter, password = line.replace(':', '').split(' ')
    fromnr, tonr = rule.split('-')
    amount = password.count(letter)
    if amount >= int(fromnr) and amount <= int(tonr):
        return True
    else:
        return False


correct = 0
for line in input:
    if checkPassword(line):
        correct += 1
print('answer to part 1:', correct)


def newPolicy(line):
    rule, letter, password = line.replace(':', '').split(' ')
    index1, index2 = rule.split('-')
    if (password[int(index1)-1] == letter and password[int(index2)-1] != letter) or \
            (password[int(index1)-1] != letter and password[int(index2)-1] == letter):
        return True
    else:
        return False


correct = 0
for line in input:
    if newPolicy(line):
        correct += 1
print('answer to part 2:', correct)
