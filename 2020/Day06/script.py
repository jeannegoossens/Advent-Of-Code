input = open('input.txt').read().split('\n\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

total_1 = 0
total_2 = 0
for group in input:
    answers = group.split('\n')
    for letter in alphabet:
        if group.count(letter) > 0:
            total_1 += 1
        everyone = 0
        for person in answers:
            if person.count(letter) > 0:
                everyone += 1
        if everyone == len(answers):
            total_2 += 1

print('solution to part 1:', total_1)
print('solution to part 2:', total_2)
