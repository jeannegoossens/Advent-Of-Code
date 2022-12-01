inp = open('inputs/Day09.txt').read()

sum = 0
depth = 1
character = 0
noncancelled = 0
while character < len(inp):
    if inp[character] == "{":
        sum += depth
        depth += 1
        character += 1
    elif inp[character] == '}':
        depth -= 1
        character += 1
    elif inp[character] == '<':
        while inp[character] != '>':
            if inp[character] == '!':
                character += 2
            else:
                noncancelled += 1
                character += 1
        noncancelled -= 1
        character += 1
    elif inp[character] == '!':
        character += 2
    else:
        character += 1

print(sum)
print(noncancelled)
