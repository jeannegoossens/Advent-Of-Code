inp = open('inputs/day16.txt').read()
bi = bin(int(inp, 16))[2:].zfill(len(inp*4))


def decode(binary, Vsum):
    if len(binary) < 11:
        return Vsum, binary
    #print('start', binary, Vsum)
    V = int(binary[:3], 2)
    binary = binary[3:]
    Vsum += V
    #print('V', V, binary)
    T = int(binary[:3],2)
    binary = binary[3:]
    #print('T', T, binary)
    if T == 4:  # literal value
        numbers = []
        while binary[0] == '1':
            numbers.append(binary[1:5])
            binary = binary[5:]
        numbers.append(binary[1:5])
        binary = binary[5:]
        #print('lit', int(''.join(numbers), 2), binary)
        return Vsum, binary
    else:   # operator
        I = binary[0]
        binary = binary[1:]
        #print('I', I, binary)
        if I == '0':
            L = int(binary[:15], 2)
            binary = binary[15:]
            #print('L', L, binary)
            leftover = len(binary) - L
            while len(binary) > leftover:
                #print('x', binary)
                Vsum, binary = decode(binary, Vsum)
        else:  # I == 1
            L = int(binary[:11], 2)
            binary = binary[11:]
            #print('L', L, binary)
            for x in range(L):
                #print('x', x)
                Vsum, binary = decode(binary, Vsum)
        return Vsum, binary


Vsum, bi = decode(bi, 0)
print(Vsum)

# part 1: 925
