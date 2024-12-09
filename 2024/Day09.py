inp = [int(i) for i in open('inputs/Day09.txt').read()]

diskmap = inp
blocks = []
compacted = []
checksum = 0

ix = 0
for idx, i in enumerate(diskmap):
    if idx % 2 == 0:
        blocks.extend([ix for j in range(i)])
        ix += 1
    elif i != 0:
        blocks.extend(['.' for j in range(i)])

clean_blocks = [b for b in blocks if b != '.']

for block in blocks:
    if len(clean_blocks) > 0:
        if block == '.':
            compacted.append(clean_blocks[-1])
            clean_blocks = clean_blocks[:-1]
        else:
            compacted.append(clean_blocks[0])
            clean_blocks = clean_blocks[1:]


for idx, c in enumerate(compacted):
    checksum += idx * c

print("Part 1:", checksum)

blocks = []
compacted = []
checksum = 0

ix = 0
for idx, i in enumerate(diskmap):
    if idx % 2 == 0:
        blocks.append([ix for j in range(i)])
        ix += 1
    elif i != 0:
        blocks.append(['.' for j in range(i)])

clean_blocks = [b for b in blocks if b[0] != '.']


def cleanup(blocks):
    newblocks = []
    last = blocks[0]
    for new in blocks[1:]:
        if new[0] == last[0]:
            last.extend(new)
        else:
            newblocks.append(last)
            last = new
    newblocks.append(last)
    return newblocks


for x, file in enumerate(reversed(clean_blocks[1:])):
    for idx, block in enumerate(blocks[:blocks.index(file)]):
        if block[0] == '.':
            if len(block) > len(file):
                blocks[blocks.index(file)] = ['.' for k in range(len(file))]
                blocks.insert(idx+1, ['.' for i in range(len(block) - len(file))])
                blocks[idx] = file
                break
            elif len(block) == len(file):
                blocks[blocks.index(file)] = ['.' for k in range(len(file))]
                blocks[idx] = file
                break
    blocks = cleanup(blocks)


compacted = [j for i in blocks for j in i]
for idx, c in enumerate(compacted):
    if c != '.':
        checksum += idx * c

print("Part 2:", checksum)
