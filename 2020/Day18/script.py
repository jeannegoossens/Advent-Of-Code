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
        inner[0] = inner[0][1:-1]
        # inner = re.findall(r'\([^\)\(]*\)', inner[0])
    if len(inner) > 0:
        for x in range(len(inner)):
            equation = equation.replace(inner[x], str(solve(inner[x])))
        return solve(equation)
    else:
        return solution(equation)


# ind = 0
# total = 0
# for line in inp:
#     sol = solve(line)
#     print(ind, 'equation', line, '=', sol)
#     total += sol
#     ind += 1
# print(total)

# 570016041025 too low
# 572361518943 too low

inp = "4 + 6 + (3 + 8 * 2 * 6 * 7 + 3)"
print(solve(inp)) # 937  (1179)

inp = "(3 * 7) + 2 * 3 + 4 + (5 * 8 + 7 + 9 * 7 * 7)"
print(solve(inp)) # 2817