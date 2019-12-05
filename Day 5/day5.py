def interpret(opcode):
    opcode = str(opcode).zfill(5)
    op = int(opcode[-2:])
    p1 = int(opcode[-3])
    p2 = int(opcode[-4])
    p3 = 0  # always 0
    return (p3, p2, p1, op)

def getvalue(numbers, i):
    while str(numbers[i]).zfill(5)[-2:] != 99:
        opcode = interpret(numbers[i])
        
        first  = numbers[numbers[i+1]] if opcode[2] == 0 else numbers[i+1]
        if opcode[3] <= 2:
            second = numbers[numbers[i+2]] if opcode[1] == 0 else numbers[i+2]
            third  = numbers[i+3]

        if opcode[3] == 1:
            numbers[third] = first + second
            i += 4
        elif opcode[3] == 2:
            numbers[third] = first * second
            i += 4
        elif opcode[3] == 3:
            numbers[numbers[i+1]] = int(input('Geef een input: '))
            i += 2
        elif opcode[3] == 4:
            print(first)
            i += 2

numbers = open('input.txt').read().split(',')
numbers = [int(i) for i in numbers]
getvalue(numbers, 0)
