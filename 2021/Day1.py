inp = [int(i) for i in open("input.txt").read().split('\n')]

prev = sum(inp[0:3])
count = 0

for i in inp[1:]:
  if i > prev:
    count += 1
  prev = i
  
print(count)
