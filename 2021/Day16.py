inp = open('inputs/day16.txt').read()
bi = bin(int(inp, 16))[2:].zfill(len(inp*4))


def decode(binary):
    if len(binary) < 11:
        return 0, binary
    V = int(binary[:3], 2)  # I dont think this matters at all in part 2
    binary = binary[3:]
    T = int(binary[:3],2)
    binary = binary[3:]
    if T == 4:  # literal value
        numbers = []
        while binary[0] == '1':
            numbers.append(binary[1:5])
            binary = binary[5:]
        numbers.append(binary[1:5])
        binary = binary[5:]
        return int(''.join(numbers), 2), binary
    else:   # operator
        I = binary[0]
        binary = binary[1:]
        if I == '0':
            L = int(binary[:15], 2)
            binary = binary[15:]
            leftover = len(binary) - L
            subscores = []
            while len(binary) > leftover:
                score, binary = decode(binary)
                subscores.append(score)
        else:  # I == 1
            L = int(binary[:11], 2)
            binary = binary[11:]
            subscores = []
            for x in range(L):
                score, binary = decode(binary)
                subscores.append(score)
        packetscore = 0
        if T == 0:
            packetscore = sum(subscores)
        elif T == 1:
            packetscore = 1
            for x in subscores:
                packetscore *= x
        elif T == 2:
            packetscore = min(subscores)
        elif T == 3:
            packetscore = max(subscores)
        elif T == 5:
            packetscore = int(subscores[0] > subscores[1])
        elif T == 6:
            packetscore = int(subscores[0] < subscores[1])
        elif T == 7:
            packetscore = int(subscores[0] == subscores[1])
        return packetscore, binary


score, bi = decode(bi)
print(score)

# part 1: 925
# part 2: 342997120375
