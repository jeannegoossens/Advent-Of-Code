type1 = [0, 1, 2,  3,  4,  6, 9]
type2 = [5, 7, 8, 10, 11, 12, 13]

params = [[10,12], [12,7], [10,8], [12,8], [11,15], [-16,12], [10,8], [-11,13], [-13,3], [13,13], [-8,3], [-1,9], [-4,4], [-14,13]]


def solve(digit, z):
    global sol
    if digit > 13:
        return z == 0
    if digit in type2:
        w = (z % 26) + params[digit][0]
        thenz = int(z/26)
        if w < 1 or w > 9:
            return False
        else:
            sol[digit] = w
            return solve(digit+1, thenz)
    else:
        for w in range(9, 0, -1):
            thenz = (26 * z) + w + params[digit][1]
            if solve(digit + 1, thenz):
                sol[digit] = w
                return True


sol = [0 for _ in range(14)]
solve(0, 0)
print(''.join(map(str, sol)))

