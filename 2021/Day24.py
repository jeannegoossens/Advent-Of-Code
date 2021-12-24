# i    0    1    2    3    4    5    6    7    8    9   10   11   12   13
Z = [  1,   1,   1,   1,   1,  26,   1,  26,  26,   1,  26,  26,  26,  26]  # z div
X = [ 10,  12,  10,  12,  11, -16,  10, -11, -13,  13,  -8,  -1,  -4, -14]  # x add
Y = [ 12,   7,   8,   8,  15,  12,   8,  13,   3,  13,   3,   9,   4,  13]  # y add
# w = [  9,   9,   9,   9,   9,   9,   9,   9,   9,   9,   9,   9,   9,   9]  # w input


def run_program(w):
    w = [int(i) for i in w]
    x, y, z = 0, 0, 0
    for instr in range(14):
        x = 0 if ((z % 26) + X[instr]) == int(w[instr]) else 1
        y = (25 if x == 1 else 0) + 1
        z = int(z / Z[instr]) * y
        z = z + ((int(w[instr]) + Y[instr]) if x == 1 else 0)
    return z == 0


modelnr = 99997258454321
result = False
while not result:
    result = run_program(str(modelnr))
    if result:
        print(modelnr, result)
        break
    if modelnr % 100000 == 54321:
        print(modelnr)
    modelnr -= 1
    while '0' in str(modelnr):
        modelnr -= 1
