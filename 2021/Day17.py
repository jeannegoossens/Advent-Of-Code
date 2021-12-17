inp = open('inputs/day17.txt').read().split(': ')[1]
x, y = inp.split(', ')
x = [int(i) for i in x.split('=')[1].split('..')]
y = [int(i) for i in y.split('=')[1].split('..')]


possible_x = []
for x_vel in range(x[1]):
    if x[0] <= int((x_vel * (x_vel+1)) / 2) <= x[1]:
        minx = x_vel
        break
possible_x = [minx]

# part 2
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


# we need to get all possible y velocities for part 1
# this is a mathematical function we can extract and simplify

# yposition = start_y_pos + starty_y_velocity + (-1 * step)
# ybounds   =       0     +        ?          + (-1 * step)
#        -? = -ybound + 0 +  (-1 * step)
#         ? = ybound  + 0 + -(-1 * step)
#         ? = ybound  + 0 + 1 * -step
#         ? = ybound - step

start_y_position = 0
possible_y_vel = []
for targetposition in range(y[0], y[1]+1):
    step = 1
    start_y_vel = 0
    while start_y_position + start_y_vel + -step >= y[0]:
        start_y_vel = -targetposition + (-1 * step)
        step += 1
        possible_y_vel.append(start_y_vel)
# now we have all possible y velocities that hit the target for part 1
# (in hindsight it doesn't but it works well enough to get the result for pt 1)
possible_y_vel = set(possible_y_vel)


def maxshoot(y_vel, x_vel):
    ypos = 0
    xpos = 0
    maxy = 0
    while ypos >= y[0] and xpos <= x[1]:
        ypos = ypos + y_vel
        xpos = xpos + x_vel
        y_vel = y_vel - 1
        x_vel = max(0, x_vel-1)
        maxy = max(maxy, ypos)
    return maxy


maxy = 0
for x_vel in possible_x:
    for y_vel in possible_y_vel:
        maxy = max(maxy, maxshoot(y_vel, x_vel))
print('part 1:', maxy)
# part 1 8646


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


# say y_velocity < the lowest bound of the target y
#   you would overshoot the target in one step
# day y_velocity >= the absolute lowest bound of the target y
#   so in the example given what if y_velocity >= 10
#   then after passing back through y_position = 0 after y_velocity steps
#   we would again completely overshoot the target in one more step
# so the possible y_velocity has to be between the lowest bound of the target y
# and the same bound in the positive spectrum, minus 1.
possible_y = [i for i in range(y[0], abs(y[0]))]
# and we know possible x already

possible_vels = 0
for x_vel in possible_x:
    for y_vel in possible_y:
        if shoot(y_vel, x_vel):
            possible_vels += 1
print('part 2:', possible_vels)
# part 2 5945
