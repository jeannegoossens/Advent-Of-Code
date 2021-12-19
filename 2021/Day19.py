import copy

# scanners = open('inputs/day19.txt').read().split('\n\n')
scanners = open('testinput.txt').read().split('\n\n')

inputscanners = [[(int(beacon.split(',')[0]), int(beacon.split(',')[1]), int(beacon.split(',')[2])) for beacon in s.split('\n')[1:]] for s in scanners]
# inputscanners is now a list of lists of tuples


class Beacon:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.distances = []

    def __add__(self, other):
        return (self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return (self.x - other.x, self.y - other.y, self.z - other.z)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z - other.z

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z + other.z)


class Scanner:
    def __init__(self, id, beacons):
        self.id = id
        self.beacons = [Beacon(b) for b in beacons]
        self.location = None
        self.orientations = []
        # if self.id != 0:
        #     self.find_orientations()
        self.find_distances()

    def __str__(self):
        return f"Scanner {self.id} at {self.location} sees beacons {len(self.beacons)} in {len(self.orientations)} orientations;"

    def turn_x(self):
        # turn along the x-axis
        # x stays the same, y is z*-1, z is y
        for beacon in self.beacons:
            tmp = beacon.z
            beacon.y = beacon.z * -1
            beacon.z = tmp
        # self.beacons = [(b.x, b.z*-1, b.y) for b in self.beacons]
        return self

    def turn_y(self):
        # x is z, y stays the same, z is x*-1
        for beacon in self.beacons:
            tmp = beacon.x
            beacon.x = beacon.z
            beacon.z = tmp * -1
        # self.beacons = [(b.z, b.y, b.x*-1) for b in self.beacons]
        return self

    def turn_z(self):
        # x is y, y is x*-1, z stays the same
        for beacon in self.beacons:
            tmp = beacon.y
            beacon.y = beacon.x * -1
            beacon.x = tmp
        # self.beacons = [(b.y, b.x*-1, b.z) for b in self.beacons]
        return self

    def find_distances(self):
        for beacon in self.beacons:
            for other in self.beacons:
                beacon.distances.append(beacon.distance_to(other))

    def find_orientations(self):
        # create a list all orientations of beacons for this cube
        for x in range(4):
            self.turn_x()
            for y in range(4):
                self.turn_y()
                for z in range(4):
                    self.turn_z()
                    if self.beacons not in self.orientations:
                        self.orientations.append(self.beacons)


def find_overlap(knowngrid, scanners, knownscanners):
    knowngrid.find_distances()
    for beacon in knowngrid.beacons:
        for scanner in scanners.values():
            if scanner.id in knownscanners:
                continue
            for other_beacon in scanner.beacons:
                overlap = list(set(beacon.distances) & set(other_beacon.distances))
                if len(overlap) >= 12:
                    print("overlap found")
                    # now what...?
                    
                    # TODO implement this somehow
                    return knowngrid, knownscanners
    raise Exception("no overlap found")


scanners = {}
for scanner in range(len(inputscanners)):
    s = Scanner(scanner, inputscanners[scanner])
    scanners[scanner] = s
scanners[0].location = (0,0,0)

print("SCANNERS INITIALLY")
for s in scanners.values():
    print(s)

knowngrid = copy.deepcopy(scanners[0])
knownscanners = [0]

print("\nDATA KNOWN AT START")
print("known grid", knowngrid)
print("known scanners", knownscanners)

print("\nSTARTING CALCULATION")
while len(knownscanners) < 2:
    knowngrid, knownscanners = find_overlap(knowngrid, scanners, knownscanners)

    print("known grid", knowngrid)
    print("known scanners", knownscanners)

print("\nSOLUTION")
print(len(set([i for i in range(len(knowngrid.beacons))])))
