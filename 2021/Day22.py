import re

inp = open('inputs/day22.txt').read().split('\n')


class Cuboid:
    def __init__(self, action, numbers):
        self.action = action
        self.xmin = numbers[0]
        self.xmax = numbers[1]
        self.ymin = numbers[2]
        self.ymax = numbers[3]
        self.zmin = numbers[4]
        self.zmax = numbers[5]

    def __repr__(self):
        return f"Cuboid with bounds x({self.xmin},{self.xmax}), y({self.ymin},{self.ymax}), z({self.zmin},{self.zmax})"


def getactive(cuboid, active):
    if cuboid.xmin >= -50 and cuboid.xmax <= 50 \
            and cuboid.ymin >= -50 and cuboid.ymax <= 50 \
            and cuboid.zmin >= -50 and cuboid.zmax <= 50:
        for x in range(cuboid.xmin, cuboid.xmax+1):
            for y in range(cuboid.ymin, cuboid.ymax+1):
                for z in range(cuboid.zmin, cuboid.zmax+1):
                    if (x,y,z) in active and cuboid.action == 'off':
                        active.discard((x,y,z))
                    elif (x,y,z) not in active and cuboid.action == 'on':
                        active.add((x,y,z))
    return active


active = set()
for line in inp:
    action = re.search(r'on|off', line).group()
    numbers = [int(n.group()) for n in re.finditer(r'([-]?[0-9]+)', line)]
    cuboid = Cuboid(action, numbers)
    active = getactive(cuboid, active)

print(len(active))

# part 1: 567496
