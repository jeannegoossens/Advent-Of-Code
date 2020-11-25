# 2015
# Day 10

input = "3113322113"

print(input)

for x in range(50):
    new = ''
    count = 1
    for i in range(len(input)):
        try:
            if input[i] != input[i+1]:
                new += str(count) + input[i]
                count = 1
            else:
                count += 1
        except IndexError:
            new += str(count) + input[i]
            break
    input = new
    print(len(new))