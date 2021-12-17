inp = open('inputs/day17.txt').read().split(': ')[1]
x, y = inp.split(', ')
x = [int(i) for i in x.split('=')[1].split('..')]
y = [int(i) for i in y.split('=')[1].split('..')]


# in hindsight after solving part 1, I realised part 1 is just this
y_vel = abs(y[0])-1  # get the highest valid y velocity (see comments below on validity)
max_y_pos = (y_vel * (y_vel + 1)) / 2  # gaussian sum
print('part 1:', max_y_pos)
# part 1 8646


# part 2
possible_x = []
for x_vel in range(x[1]):
    if x[0] <= int((x_vel * (x_vel+1)) / 2) <= x[1]:
        minx = x_vel
        break
for x_vel in range(minx, x[1]+1):
    xpos = 0
    step = 0
    while xpos <= x[1]:
        xpos += max(0, x_vel - step)
        step += 1
        if x[0] <= xpos <= x[1]:
            possible_x.append(x_vel)
            break
# now we have all possible x velocities that hit the target
possible_x = set(possible_x)

# say y_velocity < the lowest bound of the target y
#   you would overshoot the target in one step
# day y_velocity >= the absolute lowest bound of the target y
#   so in the example given what if y_velocity >= 10
#   then after passing back through y_position = 0 after y_velocity steps
#   we would again completely overshoot the target in one more step
# so the possible y_velocity has to be between the lowest bound of the target y
# and the same bound in the positive spectrum, minus 1.
possible_y = [i for i in range(y[0], abs(y[0]))]


def shoot(y_vel, x_vel):
    ypos = 0
    xpos = 0
    while ypos >= y[0] and xpos <= x[1]:
        ypos = ypos + y_vel
        xpos = xpos + x_vel
        y_vel = y_vel - 1
        x_vel = max(0, x_vel-1)
        if y[1] >= ypos >= y[0] and x[0] <= xpos <= x[1]:
            return True
    return False


possible_vels = 0
for x_vel in possible_x:
    for y_vel in possible_y:
        if shoot(y_vel, x_vel):
            possible_vels += 1
print('part 2:', possible_vels)
# part 2 5945
