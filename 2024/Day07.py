inp = open("inputs/Day07.txt").read().split('\n')

sum = 0

for line in inp:
    print()
    test, numbers = line.split(': ')
    test = int(test)
    numbers = [int(n) for n in numbers.split()]
    checks = False
    max_value = (2 ** len(numbers))
    print(test, numbers, max_value)
    for tries in range(max_value):
        s = str(numbers[0])
        product = numbers[0]
        binstr = format(tries, '0' + str(len(numbers)-1) + 'b')
        for idx, number in enumerate(numbers[1:]):
            print(binstr, tries)
            if binstr[idx] == '0':
                product += number
                s += '+' + str(number)
            else:
                product *= number
                s += '*' + str(number)
        print(s, '=', product)
        if product == test:
            print("yes", test, numbers, s)
            sum += test
            break

print("Part 1:", sum)
print("Part 2:")

# 250027429 too low