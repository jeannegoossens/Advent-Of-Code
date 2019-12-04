low = 136818
high = 685979

def checkPasswor(pw):
    if len(str(pw)) != 6:
        return False

    same = 0
    last = ''
    for char in str(pw):
        if char < last:
            return False
        if last == char:
            same += 1
        last = char

    if same == 0:
        return False
    return True

count = 0
for x in range(low, high):
    if checkPasswor(x):
        count += 1

print(count)
