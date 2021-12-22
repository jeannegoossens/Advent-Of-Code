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
        self.subcuboids = []

    def __repr__(self):
        return f"Cuboid with bounds x({self.xmin},{self.xmax}), y({self.ymin},{self.ymax}), z({self.zmin},{self.zmax})"

    def nr_cubes_off(self):
        return sum([subcuboid.nr_cubes_on() for subcuboid in self.subcuboids])

    def nr_cubes_on(self):
        return (self.xmax - self.xmin +1) * (self.ymax - self.ymin +1) * (self.zmax - self.zmin +1) - self.nr_cubes_off()

    def switch(self, other):
        overlap = find_intersections(self, other)
        if not overlap:
            return
        overlap = Cuboid('sub', overlap)
        for subcuboid in self.subcuboids:
            subcuboid.switch(overlap)
        self.subcuboids.append(overlap)


def find_intersection_on_axis(first_min, first_max, second_min, second_max):
    if first_min > second_max or second_min > first_max:
        return None
    overlap = sorted([first_min, first_max, second_min, second_max])
    return (overlap[1], overlap[2])


def find_intersections(first, second):
    x = find_intersection_on_axis(first.xmin, first.xmax, second.xmin, second.xmax)
    y = find_intersection_on_axis(first.ymin, first.ymax, second.ymin, second.ymax)
    z = find_intersection_on_axis(first.zmin, first.zmax, second.zmin, second.zmax)
    if not all((x, y, z)):
        return None
    return (x + y + z)


cuboids = []
for line in inp:
    action = re.search(r'on|off', line).group()
    numbers = [int(n.group()) for n in re.finditer(r'([-]?[0-9]+)', line)]
    new_cuboid = Cuboid(action, numbers)
    for cuboid in cuboids:
        cuboid.switch(new_cuboid)
    if new_cuboid.action == 'on':
        cuboids.append(new_cuboid)


print(sum([cuboid.nr_cubes_on() for cuboid in cuboids]))

# part 1: 567496
# part 2: 1355961721298916
