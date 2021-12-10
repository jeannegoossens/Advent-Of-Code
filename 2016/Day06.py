input = [list(line) for line in open('inputs/day06.txt').read().split('\n')]
transposed = [*zip(*input)]


def most_common(lst):
    return min(set(lst), key=lst.count)


for column in transposed:
    print(most_common(column))