genA = 873
genB = 583

facA = 16807
facB = 48271

divide = 2147483647

# part 1
matches = 0
for _ in range(40_000_000):
    genA = genA * facA % divide
    genB = genB * facB % divide
    binA = "{0:b}".format(genA)[-16:]
    binB = "{0:b}".format(genB)[-16:]
    if binA == binB:
        matches += 1

print(matches)


genA = 873
genB = 583

# part 2
matches = 0
for _ in range(5_000_000):
    genA = genA * facA % divide
    genB = genB * facB % divide
    while genA % 4 != 0:
        genA = genA * facA % divide
    while genB % 8 != 0:
        genB = genB * facB % divide
    binA = "{0:b}".format(genA)[-16:]
    binB = "{0:b}".format(genB)[-16:]
    if binA == binB:
        matches += 1

print(matches)
