input = list(map(int, open('input.txt').read().split('\n')))

from itertools import combinations


def findInvalid(input):
    for i in range(25, len(input)):
        found = False
        for c in combinations(input[i-25:i], 2):
            if sum(c) == input[i] and c[0] != c[1]:
                found = True
        if not found:
            return input[i]


def findContiguous(input, number):
    for i in range(len(input)):
        for j in range(i, len(input)):
            if sum(input[i:j]) == number:
                return min(input[i:j]) + max(input[i:j])


print('solution to part 1:', findInvalid(input))
print('solution to part 2:', findContiguous(input, findInvalid(input)))
