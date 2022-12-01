inp = {int(i.split(': ')[0]): int(i.split(': ')[1]) for i in open('inputs/Day13.txt').read().split('\n')}

# step 0 is equal to step x for length y
# y 2  x 0,  2,  4,  6,  8, 10
# y 3  x 0,  4,  8, 12, 16, 20
# y 4  x 0,  6, 12, 18, 24, 30
# y 5  x 0,  8, 16, 24, 32, 40
# y 6  x 0, 10, 20, 30, 40, 50

# for any y, stepsize = 2*(y-1)
# so for any step for any y
# you get caught if stepsize(y) % step == 0

severity = 0
for x, y in inp.items():
    stepsize = 2*(y-1)
    if x % stepsize == 0:
        severity += max(1, x*y)
print("part 1", severity)


def move(delay=0):
    for x, y in inp.items():
        stepsize = 2*(y-1)
        if (x+delay) % stepsize == 0:
            return True
    return False


free = False
delay = 0
while not free:
    caught = move(delay)
    if not caught:
        free = True
    else:
        delay += 1

print("part 2", delay)
