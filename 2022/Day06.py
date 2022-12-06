inp = list(open('inputs/Day06.txt').read())

unique = 14  # or 14 for part 2

last = inp[:unique]

for idx in range(len(inp)):
    if len(set(last)) == unique:
        print(idx)
        break
    else:
        last.pop(0)
        last.append(inp[idx])
