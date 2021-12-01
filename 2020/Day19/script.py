import re

inp = open('input.txt').read().split('\n\n')

rulebook = {r.split(': ')[0]: r.split(': ')[1] for r in inp[0].split('\n')}
messages = inp[1].split('\n')

def has_numbers(inputString):
    return any(char.isdigit() for char in inputString)

def decodeRule(rulebook, rule):
    while (has_numbers(rule)):
        for r in rule.split(' '):
            if (r.isnumeric()):
                pattern = r'\D'+ r + r'\D'
                rule = re.sub(pattern, ' ( ' + rulebook[r] + ' ) ', ' '+rule+' ').strip()
    return rule

rule = decodeRule(rulebook, rulebook['0'])
rule = rule.replace(' ', '').replace('")', '').replace('("', '')

count = 0
pattern = rule + '$'
for m in messages:
    if re.match(pattern, m):
        count += 1
print(count)

# 113 part 1
