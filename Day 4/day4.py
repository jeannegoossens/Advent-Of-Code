low = 136818
high = 685979


def checkPassword(pw):
    if len(str(pw)) != 6:
        return False

    same = 0
    current = 0
    last = '0'
    for char in str(pw):
        if last > char:
            return 0
        elif last == char:
            current += 1  # current buildup of the same character in a row
        elif last < char:  # the chain is broken
            if current == 2:  # if there were exactly two, count the occurrence
                same += 1
            current = 1  # reset current chain
        last = char

    if same > 0:  # if there was at least one occurrence of 2 equal characters in a row
        return pw
    return 0


count = 0
for x in range(low, high):
    if checkPassword(x) > 0:
        print(x)
        count += 1

print(count)
