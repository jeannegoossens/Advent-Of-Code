inp = open('input.txt').read().split('\n')

import re


def solution(equation):
    sum = 0
    operator = None
    for x in equation.split(' '):
        if x not in ['(', ')']:
            if x.isnumeric():
                if not operator:
                    sum += int(x)
                else:
                    if operator == '+':
                        sum += int(x)
                    elif operator == '*':
                        sum *= int(x)
            elif x in ['+', '*']:
                operator = x
    return sum


def solve(equation):
    inner = re.findall(r'\([^\)\(]*\)', equation)
    if len(inner) == 1:
        inner[0] = inner[0].replace('(', '').replace(')', '')
        equation = equation.replace('(' + inner[0] + ')', str(solution(inner[0])))
        return solve(equation)
    elif len(inner) > 1:
        for x in range(len(inner)):
            equation = equation.replace(inner[x], str(solve(inner[x])))
        return solve(equation)
    else:
        return solution(equation)


total = 0
for line in inp:
    sol = solve(line)
    total += sol
print('solution to part 1', total)
