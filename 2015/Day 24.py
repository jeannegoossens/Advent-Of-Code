input = """1
3
5
11
13
17
19
23
29
31
37
41
43
47
53
59
67
71
73
79
83
89
97
101
103
107
109
113"""

import itertools
import numpy

input = list(map(int, input.split('\n')))
option = [{'left': input, 'middle': [], 'right': [], 'QE': numpy.prod(input)}]
print(input)


def get_smallest(option, key):
    return min([len(x[key]) for x in option])


for i in range(len(input)):

    for seq_left in itertools.combinations(input, i):

        # test if first sequence sums to 508
        if sum(seq_left) == 508:

            # if the left pocket already contains more packages than a previous one, we don't need to look further
            if len(seq_left) > get_smallest(option, 'left'):
                continue

            # filter used packages from list
            input_filtered = [item for item in input if item not in seq_left]

            for seq_middle in itertools.combinations(input_filtered, i):

                # test if second sequence sums to 508
                if sum(seq_middle) == 508:

                    # the third pocket automatically contains all other packages and sums to 508
                    seq_right = [item for item in input_filtered if item not in seq_middle]

                    # store this sequence to a list
                    c = {'left': list(seq_left), 'middle': list(seq_middle), 'right': seq_right, 'QE': numpy.prod(seq_left)}
                    option.append(c)

print(option)
import sys
min_qe = sys.maxsize

option = option[1:]
smallest_qe = {}
for x in option:
    if x['QE'] <= min_qe:
        print(x)
        min_qe = x['QE']
        smallest_qe = x

print(smallest_qe)
# 6190437710455078891 too high
# 29728298883 too high