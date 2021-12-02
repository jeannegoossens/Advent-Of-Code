card_pc, door_pc = [int(i) for i in open('input.txt').read().split('\n')]

def doLoop(value, subjectnumber):
    value = (value * subjectnumber) % 20201227
    return value

def findLoopnumber(public_key):
    loopnumber = 0
    value = 1
    while (value != public_key):
        value = doLoop(value,7)
        loopnumber += 1
    return loopnumber

def findEncryptionKey(loopnumber, public_key):
    value = 1
    for i in range(loopnumber):
        value = doLoop(value, public_key)
    return value

# find the loopnumbers
card_ln = findLoopnumber(card_pc)
door_ln = findLoopnumber(door_pc)

# find the first encryption key and check it against the second
encryption_key = findEncryptionKey(card_ln, door_pc)
if (findEncryptionKey(door_ln, card_pc) == encryption_key):
    print(encryption_key)

# 12285001
