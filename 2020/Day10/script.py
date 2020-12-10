input = list(map(int, open('input.txt').read().split('\n')))

outlet = 0
device = max(input) + 3
input.append(outlet)
input.append(device)
input = sorted(input)

single = 0
triple = 0
for x in range(len(input) - 1):
    if input[x+1] - input[x] == 1:
        single += 1
    elif input[x+1] - input[x] == 3:
        triple += 1

print('solution to part 1:', single * triple)

valid = {i:0 for i in input}
valid[0] = 1

for i in range(1, len(input)):
    for j in range(i-3, i):
        if input[j] >= input[i]-3:
            valid[input[i]] += valid[input[j]]

# it took me forever to realize I shouldn't use input[i-3] but input[i] - 3
# have to admit I needed hints from other people for part 2
# that made me realize I had to store checked routes so I would not need to check them again for every iteration
# this storage should start at 1 though, not at 0, otherwise it will keep adding 0
# there is 1 route to the first adaptor (which is not really an adaptor but actually the outlet)

print('solution to part 2:', valid[device])
