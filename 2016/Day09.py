inp = open("inputs/day09.txt").read()

decompressed = ''
idx = 0
while idx < len(inp):
    if inp[idx] == '(':
        idx += 1
        chars = ''
        while inp[idx] != 'x':
            chars += inp[idx]
            idx += 1
        idx += 1
        times = ''
        while inp[idx] != ')':
            times += inp[idx]
            idx += 1
        idx += 1
        # print(chars, times, inp[idx:idx+int(chars)])
        repeat = inp[idx:idx+int(chars)]
        decompressed += repeat * int(times)
        idx += int(chars)
    else:
        decompressed += inp[idx]
        idx += 1

print("part 1:", len(decompressed))

