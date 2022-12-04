inp = sorted(open('input.txt').read().split('\n'))

guards = {}
i = 0
log = [[line.split('] ')[0].strip('['), line.split('] ')[1].split()] for line in inp]


def most_frequent(List):
    counter = 0
    num = List[0]
    for i in List:
        curr_frequency = List.count(i)
        if curr_frequency > counter:
            counter = curr_frequency
            num = i
    return num


while i < len(log):
    if log[i][1][1].startswith('#'):
        currentguard = log[i][1][1]
        if currentguard not in guards.keys():
            guards[currentguard] = []
    elif log[i][1][1] == 'asleep':
        start = int(log[i][0].split(':')[1])
        end = int(log[i+1][0].split(':')[1])
        guards[currentguard].extend(list(range(start,end)))
        i += 1
    i += 1

sleepiest = sorted(guards, key=lambda k: len(guards[k]), reverse=True)[0]
print("part 1:", most_frequent(guards[sleepiest]) * int(sleepiest[1:]))

most_regular = 0
the_minute = 0
the_guard = ''
for guard, sleep in guards.items():
    for i in list(set(sleep)):
        minute = most_frequent(sleep)
        if sleep.count(minute) > most_regular:
            the_guard = guard
            most_regular = sleep.count(minute)
            the_minute = minute

print("part 2:", the_minute * int(the_guard[1:]))
