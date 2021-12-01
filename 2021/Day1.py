inp = [int(i) for i in open("input.txt").read().split('\n')]

prev = sum(inp[0:3])
count = 0

for i in range(len(inp[1:])):
  if i <= len(inp)-2:
    j = sum(inp[i:i+3])
    if j > prev:
      count += 1
    prev = j
  
print(count)
