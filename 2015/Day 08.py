input = open('inputs/input08.txt')

length = 0
l = 0

for line in input:
    lit = len(line[:-1])
    mem = len(eval(line))
    new = lit + line.count('"') + line.count("\\") + 2
    length += lit - mem
    l += new - lit
length += 1  # for missing newline at end

print('part 1:', length)
print('part 2:', l)
