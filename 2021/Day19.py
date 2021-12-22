scanners = open('inputs/day19.txt').read().split('\n\n')
# scanners = open('testinput.txt').read().split('\n\n')

inputscanners = [[(int(beacon.split(',')[0]), int(beacon.split(',')[1]), int(beacon.split(',')[2]))
                  for beacon in s.split('\n')[1:]] for s in scanners]


class Scanner:
    def __init__(self, id, beacons):
        self.id = id
        self.relative_beacons = [Beacon(beacon) for beacon in beacons]
        self.absolute_beacons = None
        self.location = None
        self.calc_manhattan_distances()

    def __repr__(self):
        return f"Scanner {self.id} {self.location} with {len(self.relative_beacons)} beacons."

    def set_absolute_beacons(self, orientation, displacement):
        self.absolute_beacons = []
        for rel_beacon in self.relative_beacons:
            abs_beacon = Beacon(rel_beacon.coordinates())

            # apply the reorientation
            reoriented = abs_beacon.orientations()[orientation]
            abs_beacon.x = reoriented[0]
            abs_beacon.y = reoriented[1]
            abs_beacon.z = reoriented[2]

            # now apply the translation
            abs_beacon.x += displacement.coordinates()[0]
            abs_beacon.y += displacement.coordinates()[1]
            abs_beacon.z += displacement.coordinates()[2]

            self.absolute_beacons.append(abs_beacon)

            # set scanner location
            if self.location is None:
                self.location = (abs_beacon - Beacon(rel_beacon.orientations()[orientation])).coordinates()

        for beacon in self.absolute_beacons:
            beacon.distances = [beacon.distance_to(other) for other in self.absolute_beacons]

    def calc_manhattan_distances(self):
        for beacon in self.relative_beacons:
            beacon.distances = [beacon.distance_to(other) for other in self.relative_beacons]


class Beacon:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.distances = None

    def __repr__(self):
        return f"Beacon ({self.x}, {self.y}, {self.z})"

    def __add__(self, other):
        return Beacon((self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        return Beacon((self.x - other.x, self.y - other.y, self.z - other.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def orientations(self):
        return [
            (self.x, self.y, self.z),
            (self.x, -self.y, -self.z),   # upside down (forwards 2x)
            (-self.x, self.y, -self.z),   # turned clockwise 2x
            (-self.x, -self.y, self.z),   # dropped right 2x

            (self.x, self.z, -self.y),    # dropped backwards
            (self.x, -self.z, self.y),    # dropped forwards
            (-self.x, self.z, self.y),    # flipped, dropped forwards
            (-self.x, -self.z, -self.y),  # flipped, dropped backwards

            (self.y, self.x, -self.z),    # flipped, dropped right
            (self.y, -self.x, self.z),    # dropped right
            (-self.y, self.x, self.z),    # dropped left
            (-self.y, -self.x, -self.z),  # flipped, dropped left

            (self.y, self.z, self.x),     # dropped right, dropped backwards
            (self.y, -self.z, -self.x),   # dropped right, dropped forwards
            (-self.y, self.z, -self.x),   # dropped left, dropped backwards
            (-self.y, -self.z, self.x),   # dropped left, dropped forwards

            (self.z, self.x, self.y),     # turned counterclockwise, dropped forwards
            (self.z, -self.x, -self.y),   # turned counterclockwise, dropped backwards
            (-self.z, self.x, -self.y),   # turned clockwise, dropped backwards
            (-self.z, -self.x, self.y),   # turned clockwise, dropped forwards

            (self.z, self.y, -self.x),    # turned counterclockwise
            (self.z, -self.y, self.x),    # turned counterclockwise, upside down (dropped backwards 2x)
            (-self.z, self.y, self.x),    # turned clockwise
            (-self.z, -self.y, -self.x),  # turned clockwise, upside down (dropped forwards 2x)
        ]

    def coordinates(self):
        return (self.x, self.y, self.z)


# make Scanner objects from the input
scanners = {}
for line in range(len(inputscanners)):
    scanners[line] = Scanner(line, inputscanners[line])
scanners[0].location = (0, 0, 0)
scanners[0].set_absolute_beacons(0, Beacon((0, 0, 0)))


# track for which scanners we have identified the absolut positions
absolute_scanners = [0]


def find_pairs(first: Scanner, second: Scanner):
    pairs = []
    for first_beacon in first.absolute_beacons:
        for second_beacon in second.relative_beacons:
            if len(list(set(second_beacon.distances) & set(first_beacon.distances))) >= 11:
                pairs.append((first_beacon, second_beacon))
    if len(pairs) >= 11:
        return pairs
    return None


def locate_scanner():
    # for any unidentified scanner
    for search_scanner in scanners.values():
        if search_scanner.id not in absolute_scanners:
            # for all identified scanners
            for s_id in absolute_scanners:
                known_scanner = scanners[s_id]
                # see if there are pairs to be found between these
                pairs = find_pairs(known_scanner, search_scanner)
                if pairs:
                    return search_scanner.id, known_scanner.id, pairs


def match_orientation(pairs, known_scanner_id, new_scanner_id):
    # we can do this with any pair we found so we will take the first one
    matchpair = pairs[0]

    # loop through all orientations a beacon can have
    for index, orientation in enumerate(matchpair[1].orientations()):
        matches = 0
        # calculate how far the beacon needs to be moved in this orientation
        # to match the other beacons absolute position
        displacement = matchpair[0] - Beacon(orientation)
        for relative_beacon in scanners[new_scanner_id].relative_beacons:
            displaced_beacon = Beacon(relative_beacon.orientations()[index]) + displacement
            if displaced_beacon in scanners[known_scanner_id].absolute_beacons:
                matches += 1
        if matches >= 11:
            return index, displacement


def match_scanners():
    while len(absolute_scanners) < len(scanners.keys()):
        new_scanner_id, known_scanner_id, pairs = locate_scanner()
        orientation, displacement = match_orientation(pairs, known_scanner_id, new_scanner_id)
        absolute_scanners.append(new_scanner_id)
        scanners[new_scanner_id].set_absolute_beacons(orientation, displacement)
    return


match_scanners()

unique_beacons = set()
for scanner in scanners.values():
    for absolute_beacon in scanner.absolute_beacons:
        unique_beacons.add(absolute_beacon.coordinates())

print("Part 1:", len(unique_beacons))
# part 1: 512

max_manhatten = 0
for s1 in scanners.values():
    for s2 in scanners.values():
        manhattan = abs(s1.location[0] - s2.location[0]) + abs(s1.location[1] - s2.location[1]) + abs(s1.location[2] - s2.location[2])
        max_manhatten = max(max_manhatten, manhattan)
print("Part 2:", max_manhatten)
# part 2: 16802
