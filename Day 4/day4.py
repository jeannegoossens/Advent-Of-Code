low = 136818
high = 685979


def checkPassword(pw):
    if len(str(pw)) != 6:
        return False

    same = 0
    current = 0
    last = ''
    for char in str(pw):
        if char < last:
            return False
        if last == char:
            current += 1  # current buildup of the same character in a row
        else:  # the chain is broken
            if current == 2:  # if there were exactly two, count the occurence
                same += 1
            current = 0  # reset current chain
        last = char

    if same > 0:  # if there was at least one occurences of 2 equal characters in a row
        return True
    return False


count = 0
for x in range(low, high):
    if checkPassword(x):
        count += 1

print(count)
