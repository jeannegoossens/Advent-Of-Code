# 2015
# Day 11

# 8 lowercase
# 1 increasing straight of at least 3 letters
# may not contain i, o, or l
# must contain at least 2 different, non-overlapping pairs of letters

input = 'cqjxjnds'

alphabet = list('abcdefghijklmnopqrstuvwxyz')


def checkrules(password):
    count_doubles = 0
    straight = False
    for x in range(len(password)):
        if password[x] in ['l', 'i', 'o']:
            return False
        try:
            if password[x] == password[x+1] and password[x] != password[x+2]:
                count_doubles += 1
        except IndexError:
            break
        if straight is False and alphabet.index(password[x+1]) - alphabet.index(password[x]) == 1:
            try:
                if alphabet.index(password[x+2]) - alphabet.index(password[x+1]) == 1:
                    straight = True
            except IndexError:
                break
    if straight is False or count_doubles < 2:
        return False
    else:
        return True


def increase(password):
    pw = list(password)
    if(alphabet.index(pw[-1])) == 25:
        pw[-1] = alphabet[0]
        if (alphabet.index(pw[-2])) == 25:
            pw[-2] = alphabet[0]
            if (alphabet.index(pw[-3])) == 25:
                pw[-3] = alphabet[0]
                if (alphabet.index(pw[-4])) == 25:
                    pw[-4] = alphabet[0]
                    if (alphabet.index(pw[-5])) == 25:
                        pw[-5] = alphabet[0]
                        if (alphabet.index(pw[-6])) == 25:
                            pw[-6] = alphabet[0]
                            if (alphabet.index(pw[-7])) == 25:
                                pw[-7] = alphabet[0]
                                if (alphabet.index(pw[-8])) == 25:
                                    return 'max'
                                else:
                                    pw[-8] = alphabet[alphabet.index(pw[-8]) + 1]
                            else:
                                pw[-7] = alphabet[alphabet.index(pw[-7]) + 1]
                        else:
                            pw[-6] = alphabet[alphabet.index(pw[-6]) + 1]
                    else:
                        pw[-5] = alphabet[alphabet.index(pw[-5]) + 1]
                else:
                    pw[-4] = alphabet[alphabet.index(pw[-4]) + 1]
            else:
                pw[-3] = alphabet[alphabet.index(pw[-3]) + 1]
        else:
            pw[-2] = alphabet[alphabet.index(pw[-2])+1]
    else:
        pw[-1] = alphabet[alphabet.index(pw[-1])+1]
    return ''.join(pw)

while input != 'max':
    input = increase(input)
    if (checkrules(input)):
        print(input, 'correct')
        break