inp = open("inputs/day8.txt").read().split('\n')
rows = [{'input': i.split(' | ')[0].split(' '), 'output': i.split(' | ')[1].split(' ')} for i in inp]


# part 1
count = 0
for r in rows:
    r = r['output']
    for o in r:
        if len(o) in [2,4,3,7]:
            count += 1
print('part 1: ', count)


# part 2
correct = {
    0: 'abcefg',   # 6
    1: 'cf',       # 2
    2: 'acdeg',    # 5
    3: 'acdfg',    # 5
    4: 'bcdf',     # 4
    5: 'abdfg',    # 5
    6: 'abdefg',   # 6
    7: 'acf',      # 3
    8: 'abcdefg',  # 7
    9: 'abcdfg'}   # 6
correct = {v: k for k, v in correct.items()}


def decode(row):
    segments = {l: '' for l in 'abcdefg'}

    # I can find all numbers which have a unique length
    nr1 = list([i for i in row['input'] if len(i) == 2][0])
    nr4 = list([i for i in row['input'] if len(i) == 4][0])
    nr7 = list([i for i in row['input'] if len(i) == 3][0])
    nr8 = list([i for i in row['input'] if len(i) == 7][0])
    # print('found nr1', ''.join(nr1))
    # print('found nr4', ''.join(nr4))
    # print('found nr7', ''.join(nr7))
    # print('found nr8', ''.join(nr8))

    # the other numbers have one of two lengths
    len5 = [i for i in row['input'] if len(i) == 5]
    len6 = [i for i in row['input'] if len(i) == 6]

    # now I can find segment a
    for l in nr7:
        if l not in nr1:
            segments['a'] = l
            # print('found segment a', segments['a'])

    # nr3 is where length is 5 and both of nr1 appears
    nr3 = list([i for i in len5 if nr1[0] in i and nr1[1] in i][0])
    # print('found nr3', ''.join(nr3))

    # nr6 is where length is 6 and only one of nr1 appears
    nr6 = list([i for i in len6 if (nr1[0] in i and nr1[1] not in i) or (nr1[0] not in i and nr1[1] in i)][0])
    # print('found nr6', ''.join(nr6))

    # now I can find segment f and c
    if nr1[0] in nr6:
        segments['f'] = nr1[0]
        segments['c'] = nr1[1]
    else:
        segments['c'] = nr1[0]
        segments['f'] = nr1[1]
    # print('found segment c', segments['c'])
    # print('found segment f', segments['f'])

    # nr5 is where length is 5 and segment f appears
    nr5 = list([i for i in len5 if segments['f'] in i and segments['c'] not in i][0])
    # print('found nr5', ''.join(nr5))

    # nr2 is where length is 5 and nr is not nr3 or nr5
    nr2 = list([i for i in len5 if list(i) != nr5 and list(i) != nr3][0])
    # print('found nr2', ''.join(nr2))

    # now I can find bar e
    for l in nr6:
        if l in nr2 and l not in nr5 and l not in nr3:
            segments['e'] = l
            # print('found segment e', segments['e'])

    # nr9 is where length is 6 and segment e does not appear
    nr9 = list([i for i in len6 if segments['e'] not in list(i)][0])
    # print('found nr9', ''.join(nr9))

    # nr0 is where length is 6 and nr is not nr9 or nr6
    nr0 = list([i for i in len6 if list(i) != nr6 and list(i) != nr9][0])
    # print('found nr0', ''.join(nr0))

    # now I can find segment d
    for l in nr8:
        if l not in nr0:
            segments['d'] = l
            # print('found segment d', segments['d'])

    # now I can find segment b
    for l in nr4:
        if l != segments['c'] and l != segments['d'] and l != segments['f']:
            segments['b'] = l
            # print('found segment b', segments['b'])

    # now I can find segment g
    for l in nr0:
        if l != segments['a'] and l != segments['b'] and l != segments['c']\
                and l != segments['e'] and l != segments['f']:
            segments['g'] = l
            # print('found segment g', segments['g'])

    segments = {v: k for k,v in segments.items()}

    return segments


total = 0
for row in rows:
    segments = decode(row)

    out = []
    for word in row['output']:
        new = ''
        for l in word:
            new += segments[l]
        out.append(new)
    outp = ''
    for x in out:
        outp += str(correct[''.join(sorted(x))])

    total += int(outp)

print('part 2:', total)
