inp = open("input.txt").read().split('\n')

x = 0
y = 0

for i in inp:
  direction, distance = i.split(' ')
  if direction == 'up':
    y -= int(distance)
  elif direction == 'down':
    y += int(distance)
  elif direction == 'forward':
    x += int(distance)

print (x*y)

# 1670340 part 1
