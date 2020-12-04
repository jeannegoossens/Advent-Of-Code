input = open('input.txt').read().split('\n\n')

import re

fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def validateField(key, value):
    if value.isnumeric():
        if key == 'byr' and (1920 <= int(value) <= 2002):
            return True
        if key == 'iyr' and (2010 <= int(value) <= 2020):
            return True
        if key == 'eyr' and (2020 <= int(value) <= 2030):
            return True
    if key == 'hgt' and ((value[-2:] == 'cm' and 150 <= int(value[:-2]) <= 193) or (value[-2:] == 'in' and 59 <= int(value[:-2]) <= 76)):
        return True
    if key == 'hcl' and re.match('#[a-f0-9]{6}', value):
        return True
    if key == 'ecl' and value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return True
    if key == 'pid' and value.isnumeric() and len(value) == 9 and re.match('[0-9]{9}', value):
        return True
    if key == 'cid':
        return True
    return False


def checkPassport(pp):
    checks = {k:v for k,v in [x.split(':') for x in re.split(' |\n', pp)]}
    for f in fields[:-1]:
        if f not in checks.keys():
            return False
    # for part 2, check:
    for k, v in checks.items():
        if not(validateField(k,v)):
            return False
    return True


valid = 0
for line in input:
    if checkPassport(line):
        valid += 1

print(valid)
