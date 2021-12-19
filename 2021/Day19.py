# scanners = open('inputs/day19.txt').read().split('\n\n')
scanners = open('testinput.txt').read().split('\n\n')

inputscanners = [[(int(beacon.split(',')[0]), int(beacon.split(',')[1]), int(beacon.split(',')[2])) for beacon in s.split('\n')[1:]] for s in scanners]
# inputscanners is now a list of lists of tuples


class Scanner:
    def __init__(self, id, beacons):
        self.id = id
        self.beacons = beacons
        self.location = None
        self.orientations = []
        if self.id != 0:
            self.find_orientations()

    def __str__(self):
        return f"Scanner {self.id} at {self.location} sees beacons {len(self.beacons)} in {len(self.orientations)} orientations: {self.beacons};"

    def turn_x(self):
        # turn along the x-axis
        # x stays the same, y is z*-1, z is y
        self.beacons = [(b[0], b[2]*-1, b[1]) for b in self.beacons]
        return self

    def turn_y(self):
        # x is z, y stays the same, z is x*-1
        self.beacons = [(b[2], b[1], b[0]*-1) for b in self.beacons]
        return self

    def turn_z(self):
        # x is y, y is x*-1, z stays the same
        self.beacons = [(b[1], b[0]*-1, b[2]) for b in self.beacons]
        return self

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


# voor elke anchor beacon in knowngrid
#   voor elke andere scanner
#     voor elke orientatie
#       voor elke anchor beacon in die andere scanner
#         als overlap >= 12
#           smash grids together into knowngrid
def find_overlap(knowngrid, scanners, knownscanners):
    for known_beacon in knowngrid:
        relative_known_beacons = [tuple(map(lambda i, j: i - j, t, known_beacon)) for t in knowngrid]
        for scanner in [scanners[4]]:
            if scanner.id in knownscanners:
                continue
            for oriented_beacons in s.orientations:
                for other_beacon in oriented_beacons:
                    relative_other_beacons = [tuple(map(lambda i, j: i - j, t, other_beacon)) for t in oriented_beacons]
                    overlap = list(set(relative_known_beacons) & set(relative_other_beacons))
                    if len(overlap) >= 10:
                        print(sorted(overlap))
                        for j in relative_other_beacons:
                            knowngrid.append((j[0]+known_beacon[0], j[1]+known_beacon[1], j[2]+known_beacon[2]))
                        scanner.location = (other_beacon[0] + known_beacon[0],
                                            other_beacon[1] + known_beacon[1],
                                            other_beacon[2] + known_beacon[2])
                        knownscanners.append(scanner.id)
                        knowngrid = list(set(knowngrid))
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

knowngrid = scanners[1].beacons.copy()
knownscanners = [1]

print("\nDATA KNOWN AT START")
print("known grid", knowngrid)
print("known scanners", knownscanners)

print("\nSTARTING CALCULATION")
while len(knownscanners) < 2:
    knowngrid, knownscanners = find_overlap(knowngrid, scanners, knownscanners)

    print("known grid", knowngrid)
    print("known scanners", knownscanners)

print("solution:", len(set(knowngrid)))
