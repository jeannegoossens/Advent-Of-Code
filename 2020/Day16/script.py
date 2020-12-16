input = open('inp.txt').read().split('\n\n')

ticket = list(map(int, input[1].split('\n')[1].split(',')))

others = [list(map(int, o.split(','))) for o in input[2].split('\n')[1:]]

rules = {x.split(': ')[0] : x.split(': ')[1].split(' or ') for x in input[0].split('\n')}
rules = {k : [list(map(int, a.split('-'))) for a in v] for k,v in rules.items()}

print('ticket', ticket)
print('others', others)
print('rules', rules)


def check_number(n, check):
    if check[0][0] <= n <= check[0][1] or check[1][0] <= n <= check[1][1]:
        return True
    return False


invalids = []
for other in others:
    for number in other:
        valid = False
        for rule, check in rules.items():
            if check_number(number, check):
                valid = True
        if not valid:
            invalids.append(number)

print('\nsolution to part 1:', sum(invalids))

# 25895
