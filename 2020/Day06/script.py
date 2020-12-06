input = open('input.txt').read().split('\n\n')

alphabet = 'abcdefghijklmnopqrstuvwxyz'

total = 0
for group in input:
    answers = group.split('\n')
    for letter in alphabet:
        everyone = 0
        for person in answers:
            if person.count(letter) > 0:
                everyone += 1
        if everyone == len(answers):
            total += 1

print(total)
