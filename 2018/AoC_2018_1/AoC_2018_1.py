lines = open("input.txt").read().split('\n')
lines = list(filter(None, lines))

freq = 0
print("Frequency to start at is %d" % freq)

allfreqs = []
found = False

round = 0
while(not(found)):
    for x in lines:
        if x[0] == '+':
            freq += int(x[1:])
        else:
            freq -= int(x[1:])
        if (freq in allfreqs):
            print(freq)
            found = True
            break
        allfreqs.append(freq)
    round += 1
    print("new round: %s" % round)
