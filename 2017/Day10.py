inp = [int(i) for i in open('inputs/Day10.txt').read().split(',')]
print(inp)
current = 0
skipsize = 0
lengths = [i for i in range(256)]

for l in inp:
    print()
    print('current', current, ', l', l, ', skipssize', skipsize)
    if current + l > len(lengths):
        sub = lengths[current:]
        short = l - len(sub)
        sub.extend(lengths[:(current + l) % len(lengths)])
        print('sub', sub, 'short', short)
        print('rsub', list(reversed(sub)))
        new = list(reversed(sub))[l - short:]
        print('n',new)
        new.extend(lengths[l - short:current])
        print('n',new)
        new.extend(list(reversed(sub))[:l-short])
        print('n',new)
    else:
        sub = lengths[current:current + l]
        print('sub', sub)
        new = lengths[:current]
        new.extend(reversed(sub))
        new.extend(lengths[current + l:])
    current += l + skipsize
    current = current % len(lengths)
    skipsize += 1
    lengths = new

    print('ls', lengths)
print(lengths[0] * lengths[1])

# 32942 too high
# 14762 too low

# the order is set right but not the positions of the numbers
# they are not replaced at the same indexes
