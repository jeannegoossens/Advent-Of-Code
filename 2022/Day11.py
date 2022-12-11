from functools import reduce

inp = [i.split('\n') for i in open('inputs/Day11.txt').read().split('\n\n')]


def parse_input(inp):
    monkeys = {}
    for monkey in inp:
        idx = monkey[0][:-1].split(' ')[-1]
        edit = monkey[2].split(' = ')[1].split(' ')[-1]
        edit = int(edit) if edit.isnumeric() else 0
        monkeys[idx] = {
            'items': [int(i) for i in monkey[1].split(': ')[1].split(',')],
            'oper': monkey[2].split(' = ')[1].split(' ')[-2],
            'edit': edit,
            'test': int(monkey[3].split(' ')[-1]),
            'true': monkey[4].split(' ')[-1],
            'false': monkey[5].split(' ')[-1]
        }
    return monkeys


def do_round(monkeys, worry=True):
    for key in monkeys.keys():
        monkey = monkeys[key]
        for item in monkey['items']:
            edit = monkey['edit'] if monkey['edit'] != 0 else item
            if monkey['oper'] == '+':
                item = item + edit
            elif monkey['oper'] == '*':
                item = item * edit
            if worry:
                counted_1[key] += 1
                item = item // 3
            else:
                counted_2[key] += 1
                if item > max_int:
                    item = item % max_int
            if item % monkey['test'] == 0:
                monkeys[monkey['true']]['items'].append(item)
            else:
                monkeys[monkey['false']]['items'].append(item)
        monkey['items'] = []
    return monkeys


# part 1
monkeys_1 = parse_input(inp)
counted_1 = {k: 0 for k in monkeys_1.keys()}

for r in range(20):
    monkeys_1 = do_round(monkeys_1, True)

counted_1 = sorted([v for v in counted_1.values()])
print("part 1:", counted_1[-1] * counted_1[-2])
# 54054


# part 2
monkeys_2 = parse_input(inp)
counted_2 = {k: 0 for k in monkeys_2.keys()}

# need to keep big numbers small, so mod it with the product of all mod operations of the monkeys
# this reduces the big numbers to any number between 0 and the product of all mod operations
mod_numbers = [v['test'] for v in monkeys_2.values()]
max_int = reduce((lambda x, y: x * y), mod_numbers)

for r in range(10_000):
    monkeys_2 = do_round(monkeys_2, False)

counted_2 = sorted([v for v in counted_2.values()])
print("part 2:", counted_2[-1] * counted_2[-2])
# 14314925001
