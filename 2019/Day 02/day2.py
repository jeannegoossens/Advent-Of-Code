numbers = open('input.txt').read().split(',')
numbers = [int(i) for i in numbers]


def calculate(input, noun, verb):
    input[1] = noun
    input[2] = verb
    i = 0
    while input[i] != 99:
        try:
            if input[i] == 1:
                input[input[i + 3]] = input[input[i + 1]] + input[input[i + 2]]
            elif input[i] == 2:
                input[input[i + 3]] = input[input[i + 1]] * input[input[i + 2]]
        except:
            pass
        i += 4
    return input[0]


answer = 19690720

for noun in range(0, 100):
    for verb in range(0, 100):
        iteration = numbers[:]
        test = calculate(iteration, noun, verb)
        if test == answer:
            print(100 * noun + verb)
            exit()
