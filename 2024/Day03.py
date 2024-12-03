import re

inp = ''.join(open('inputs/Day03.txt').read().split('\n'))
muls_1 = [(int(i[0]), int(i[1])) for i in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", inp)]

# part 2: split the input by the do's, then cut off anything that follows a don't
inp_2 = ''.join([i.split("don't()")[0] for i in inp.split("do()")])
muls_2 = [(int(i[0]), int(i[1])) for i in re.findall(r"mul\(([0-9]{1,3}),([0-9]{1,3})\)", inp_2)]

print("Part 1:", sum([mul[0] * mul[1] for mul in muls_1]))
print("Part 2:", sum([mul[0] * mul[1] for mul in muls_2]))
