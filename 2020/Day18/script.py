inp = open('input.txt').read().split('\n')

import re


def solution(equation):
    additions = re.findall(r'([\d]+(?:[\s]{1}\+[\s]{1}[\d]+)+)', equation)
    for addition in additions:
        a = sum([int(u) for u in addition.split(' ') if u.isnumeric()])
        equation = equation.replace(addition, str(a) + ' ')

    fullsum = 0
    operator = None
    for x in equation.split(' '):
        if x.isnumeric():
            if not operator:
                fullsum += int(x)
            else:
                if operator == '*':
                    fullsum *= int(x)
        elif x == '*':
            operator = x

    return fullsum


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


# 701339185745 part 1

total = 0
for line in inp:
    sol = solve(line)
    print(line, '=', sol)
    total += sol
print('solution to part 2', total)

# 4208490449905 part 2
