# instructions = [i.split(' ') for i in open('inputs/day24.txt').read().split('\n')]


def run_program(modelnr):
    z = 0
    w = int(modelnr[0])
    z = (int(z / 1) * (25 * (((z % 26) + 10 == w) == 0) + 1)) + ((w + 12) * (((z % 26) + 10 == w) == 0))
    w = int(modelnr[1])
    z = (int(z / 1) * (25 * (((z % 26) + 12 == w) == 0) + 1)) + ((w + 7) * (((z % 26) + 12 == w) == 0))
    w = int(modelnr[2])
    z = (int(z / 1) * (25 * (((z % 26) + 10 == w) == 0) + 1)) + ((w + 8) * (((z % 26) + 10 == w) == 0))
    w = int(modelnr[3])
    z = (int(z / 1) * (25 * (((z % 26) + 12 == w) == 0) + 1)) + ((w + 8) * (((z % 26) + 12 == w) == 0))
    w = int(modelnr[4])
    z = (int(z / 1) * (25 * (((z % 26) + 11 == w) == 0) + 1)) + ((w + 15) * (((z % 26) + 11 == w) == 0))
    w = int(modelnr[5])
    z = (int(z / 26) * (25 * (((z % 26) + -16 == w) == 0) + 1)) + ((w + 12) * (((z % 26) + -16 == w) == 0))
    w = int(modelnr[6])
    z = (int(z / 1) * (25 * (((z % 26) + 10 == w) == 0) + 1)) + ((w + 8) * (((z % 26) + 10 == w) == 0))
    w = int(modelnr[7])
    z = (int(z / 26) * (25 * (((z % 26) + -11 == w) == 0) + 1)) + ((w + 13) * (((z % 26) + -11 == w) == 0))
    w = int(modelnr[8])
    z = (int(z / 26) * (25 * (((z % 26) + -13 == w) == 0) + 1)) + ((w + 3) * (((z % 26) + -13 == w) == 0))
    w = int(modelnr[9])
    z = (int(z / 1) * (25 * (((z % 26) + 13 == w) == 0) + 1)) + ((w + 13) * (((z % 26) + 13 == w) == 0))
    w = int(modelnr[10])
    z = (int(z / 26) * (25 * (((z % 26) + -8 == w) == 0) + 1)) + ((w + 3) * (((z % 26) + -8 == w) == 0))
    w = int(modelnr[11])
    z = (int(z / 26) * (25 * (((z % 26) - 1 == w) == 0) + 1)) + ((w + 9) * (((z % 26) - 1 == w) == 0))
    w = int(modelnr[12])
    z = (int(z / 26) * (25 * (((z % 26) - 4 == w) == 0) + 1)) + ((w + 4) * (((z % 26) - 4 == w) == 0))
    w = int(modelnr[13])
    z = (int(z / 26) * (25 * (((z % 26) - 14 == w) == 0) + 1)) + ((w + 13) * (((z % 26) - 14 == w) == 0))
    return z == 0


modelnr = 99999999999999
result = False
while not result:
    result = run_program(str(modelnr))
    if result:
        print(modelnr, result)
    if modelnr % 100000 == 54321:
        print(modelnr)
    modelnr -= 1
    while '0' in str(modelnr):
        modelnr -= 1
