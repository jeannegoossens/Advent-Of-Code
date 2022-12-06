inp = list(open('inputs/Day06.txt').read())

unique = 4  # or 14 for part 2

for idx in range(len(inp)):
    if len(set(inp[idx:idx+unique])) == unique:
        print(idx+unique)
        break
