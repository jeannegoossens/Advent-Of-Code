inp = open('inputs/Day05.txt').read().split('\n\n')

rules = [i.split('|') for i in inp[0].split('\n')]
updates = [i.split(',') for i in inp[1].split('\n')]

sum = 0
direction = [rules[0][0]]

for update in updates:
    correct = True
    for idx, number in enumerate(update):
        if correct:
            for rule in rules:
                if correct:
                    if number == rule[0]:
                        if rule[1] in update and update.index(rule[1]) <= idx:
                            correct = False
                    elif number == rule[1]:
                        if rule[0] in update and update.index(rule[0]) >= idx:
                            correct = False
    if correct:
        sum += int(update[int(len(update) / 2)])

print("Part 1:", sum)
print("Part 2:")
