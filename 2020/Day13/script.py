input = open('input.txt').read().split('\n')

# part 1
time = int(input[0])
buses = sorted([int(b) for b in input[1].split(',') if b != 'x'])
bus = False
while not bus:
    for b in buses:
        if time % b == 0:
            print('solution to part 1:', (time - int(input[0])) * b)
            bus = True
    time += 1

# part 2
buses = input[1].split(',')

step = 1
time = 0

# we loop through the buses from the first to the last
# we need the buses index as well for this, because x-buses count as well
for index in range(len(buses)):
    # if the bus is x, we can ignore it and move on to the next index
    if buses[index] == 'x':
        continue
    # for each bus with a number we will count upwards from the current time
    while True:
        # once we find a time that can be divided by this bus, we can move on
        if (time + index) % int(buses[index]) == 0:
            break
        # otherwise we will move on to the next time to check it
        # we increase the time with the set stepsize, not by 1
        time += step
    # we need to increase step size for every bus that is not x.
    # this is because we want to keep the pattern alive
    # we want to skip across time with step that will ensure that previous buses also remain valid
    # so after a while step = 1 * buses[0] * buses[1] ... etc (except buses which are x)
    step *= int(buses[index])

# when we checked all buses, we know at what time they first leave consequently
print('solution to part 2:', time)
