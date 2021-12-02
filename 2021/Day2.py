inp = open("input.txt").read().split('\n')

x = 0
y = 0
aim = 0

for i in inp:
  direction, distance = i.split(' ')
  if direction == 'up':
    aim -= int(distance)
  elif direction == 'down':
    aim += int(distance)
  elif direction == 'forward':
    x += int(distance)
    y += int(distance) * aim

print (x*y)

# 1670340 part 1
# 1954293920 part 2
