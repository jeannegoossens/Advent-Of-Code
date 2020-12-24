input = open('input.txt').read().split('\n\n')

ticket = list(map(int, input[1].split('\n')[1].split(',')))

others = [list(map(int, o.split(','))) for o in input[2].split('\n')[1:]]

rules = {x.split(': ')[0] : x.split(': ')[1].split(' or ') for x in input[0].split('\n')}
rules = {k : [list(map(int, a.split('-'))) for a in v] for k,v in rules.items()}


def check_number(n, check):
    if check[0][0] <= n <= check[0][1] or check[1][0] <= n <= check[1][1]:
        return True
    return False


valid = []
invalids = []
for other in others:
    ticket_valid = True
    for number in other:
        number_valid = False
        for rule, check in rules.items():
            if check_number(number, check):
                number_valid = True
        if not number_valid:
            invalids.append(number)
            ticket_valid = False
    if ticket_valid:
        valid.append(other)

print('solution to part 1:', sum(invalids))


def check_column(column, check):
    for c in column:
        if not check_number(c, check):
            return False
    return True


columns = [*zip(*valid)]

myticket = {}

for rule, check in rules.items():
    myticket[rule] = []
    for i in range(len(columns)):
        if check_column(list(columns[i]), check):
            myticket[rule].append(i)  # used to be ticket[i]

myticket = {k: v for k, v in sorted(myticket.items(), key=lambda item: len(item[1]))}

positions = {}

for k, v in myticket.items():
    for i in v:
        if i not in positions:
            positions[i] = k

product = 1
for k, v in positions.items():
    if v.startswith('departure'):
        product *= ticket[k]

print('solution to part 2:', product)
