import itertools
import numpy as np

input = list(map(int, open('input.txt').read().split('\n')))

for x in itertools.combinations(input, 3):
    if sum(x) == 2020:
        print('found combination', x, 'with product', np.prod(x))
