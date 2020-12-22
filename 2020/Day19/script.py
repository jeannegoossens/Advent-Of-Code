input = open('inp.txt').read().split('\n\n')

testinput = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb""".split('\n\n')

rules = {r.split(': ')[0]: r.split(': ')[1] for r in testinput[0].split('\n')}
messages = testinput[1].split('\n')

print(rules)
print(messages)


def read_rule(rule_id, rulebook):
    rule = rulebook[rule_id]
    rule = rule.split(' | ')
    rule = [x.split(' ') for x in rule]
    print(rule_id, rule)
    return rule


def apply_rule(rule_id, rulebook, message, index):
    rule = read_rule(rule_id, rulebook)
    for option in rule:
        for rule_id in option:
            print(type(rule_id))
            if rule_id in ["a", "b"]:
                print('rule', rule_id, 'is character')
                if message[index] == rule_id:
                    return 1
                else:
                    return 0
            else:
                print('applying rule', rule_id, 'to message', message, 'at index', index, '(', message[index:], ')')
                index += apply_rule(rule_id, rulebook, message, index)


def checkMessage(message, rulebook):
    index = 0
    apply_rule('0', rulebook, message, index)


for message in messages:
    print(message)
    checkMessage(message, rules)
    break
