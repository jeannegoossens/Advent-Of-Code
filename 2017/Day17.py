stepsize = 324

buffer = [0]
index = 0

for x in range(1, 50_000_001):
    index = (index + stepsize) % len(buffer)
    buffer.insert(index+1, x)
    index += 1

print(buffer[buffer.index(0)+1])
