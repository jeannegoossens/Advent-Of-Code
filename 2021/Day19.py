# scanners = open('inputs/day19.txt').read().split('\n\n')
scanners = open('testinput.txt').read().split('\n\n')

inputscanners = [[(int(beacon.split(',')[0]), int(beacon.split(',')[1]), int(beacon.split(',')[2])) for beacon in s.split('\n')[1:]] for s in scanners]


class Scanner:
    def __init__(self, id, beacons):
        self.id = id
        self.location = None
        self.beacons = {beacon: Beacon(beacon) for beacon in beacons}
        for beacon in self.beacons.values():
            self.calc_distances(beacon)
        self.translation = None
        self.orientation = None

    def __repr__(self):
        return f"Scanner {self.id} at {self.location} with {len(self.beacons)} beacons, oriented {self.orientation} at translation {self.translation}"

    def calc_distances(self, beacon):
        beacon.distances = [beacon.distance_to(other) for other in self.beacons.values()]

    def reorient_beacons(self, orientation_idx):
        for beacon in self.beacons.values():
            beacon.reorient(orientation_idx)


class Beacon:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        self.ox = coordinates[0]
        self.oy = coordinates[1]
        self.oz = coordinates[2]
        self.distances = None

    def __repr__(self):
        return f"Beacon ({self.x}, {self.y}, {self.z})"

    def orientations(self):
        return [
            (self.ox, self.oy, self.oz),
            (self.ox, -self.oy, -self.oz),  # upside down (forwards 2x)
            (-self.ox, self.oy, -self.oz),  # turned clockwise 2x
            (-self.ox, -self.oy, self.oz),  # dropped right 2x

            (self.ox, self.oz, -self.oy),  # dropped backwards
            (self.ox, -self.oz, self.oy),  # dropped forwards
            (-self.ox, self.oz, self.oy),  # flipped, dropped forwards
            (-self.ox, -self.oz, -self.oy),  # flipped, dropped backwards

            (self.oy, self.ox, -self.oz),  # flipped, dropped right
            (self.oy, -self.ox, self.oz),  # dropped right
            (-self.oy, self.ox, self.oz),  # dropped left
            (-self.oy, -self.ox, -self.oz),  # flipped, dropped left

            (self.oy, self.oz, self.ox),  # dropped right, dropped backwards
            (self.oy, -self.oz, -self.ox),  # dropped right, dropped forwards
            (-self.oy, self.oz, -self.ox),  # dropped left, dropped backwards
            (-self.oy, -self.oz, self.ox),  # dropped left, dropped forwards

            (self.oz, self.ox, self.oy),  # turned counterclockwise, dropped forwards
            (self.oz, -self.ox, -self.oy),  # turned counterclockwise, dropped backwards
            (-self.oz, self.ox, -self.oy),  # turned clockwise, dropped backwards
            (-self.oz, -self.ox, self.oy),  # turned clockwise, dropped forwards

            (self.oz, self.oy, -self.ox),  # turned counterclockwise
            (self.oz, -self.oy, self.ox),  # turned counterclockwise, upside down (dropped backwards 2x)
            (-self.oz, self.oy, self.ox),  # turned clockwise
            (-self.oz, -self.oy, -self.ox),  # turned clockwise, upside down (dropped forwards 2x)
        ]

    def reorient(self, orientation_idx):
        reorientation = self.orientations()[orientation_idx]
        self.x = reorientation[0]
        self.y = reorientation[1]
        self.z = reorientation[2]

    def __add__(self, other):
        return Beacon((self.x + other.x, self.y + other.y, self.z + other.z))

    def __sub__(self, other):
        return Beacon((self.x - other.x, self.y - other.y, self.z - other.z))

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def distance_to(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y) + abs(self.z - other.z)

    def coordinates(self):
        return (self.x, self.y, self.z)


# Loading all scanners into a dictionary based on scanner id
scanners = {}
for i in range(len(inputscanners)):
    s = Scanner(i, inputscanners[i])
    scanners[i] = s
scanners[0].location = (0,0,0)

# Track for which scanners we already know the absolute positions
known_scanners = [0]


# Find matching beacons between scanners based on their absolute distances to other beacons
def find_pairs():
    # print("Find new pairs. We already know scanners:", known_scanners)
    for known_scanner in known_scanners:
        known_scanner = scanners[known_scanner]
        for scanner in scanners.values():
            if scanner.id not in known_scanners:
                # print("\tSearching for scanner", scanner.id, "on known scanner", known_scanner.id)
                pairs = []
                for beacon in known_scanner.beacons.values():
                    for other_beacon in scanner.beacons.values():
                        if len(list(set(beacon.distances) & set(other_beacon.distances))) >= 11:
                            pairs.append((beacon, other_beacon))
                if len(pairs) >= 11:
                    print(f"\nFound {len(pairs)} pairs between known scanner {known_scanner.id} and scanner {scanner.id}")
                    known_scanners.append(scanner.id)
                    return pairs, known_scanner.id, scanner.id


# Now for each orientation of the pairs from the scanner we have matched, we need to check whether the translation between all pairs is equal to find the correct orientation of the scanner
# for any pair (we take the first one for simplicity)
#     for each orientation of the second beacon of that pair
#         calculate the displacement of the second beacon
#         for every beacon in the scanner we are matching
#             calculate what absolute position it woud have if in the same orientation and with the same displacement as the second beacon in the pair
#             if that position occurs in the known grid, we have found a matching beacon
#         if we have found enough matches, we know the right orientation for this scanner
def matchOrientation(pairs, known_scanner, scanner_id):
    # print("Find matching orientation of the newest scanner on existing scanner:", known_scanner, scanner_id)
    pair = pairs[0]
    for idx, orientation in enumerate(pair[1].orientations()):
        matches = 0
        displacement = pair[0] - Beacon(orientation)
        for beacon in scanners[scanner_id].beacons.values():
            displaced = Beacon(beacon.orientations()[idx]) + displacement
            if displaced in scanners[known_scanner].beacons.values():
                matches += 1
        if matches >= 11:
            # print("\tMatch found at orientation", idx)
            return idx
    # print("No matching orientation found?")


# Now we know the right orientation of this new scanner, we can turn all beacons into that orientation, then calculate their absolute positions, and add those to the known beacon locations
# We can calculate their absolute positions by taking their relative position and adding the distance between the first pairs both beacons
def locate_scanner():
    # print("Locate the next scanner")
    pairs, known_scanner, scanner_id = find_pairs()
    correct_orientation = matchOrientation(pairs, known_scanner, scanner_id)
    scanners[scanner_id].reorient_beacons(correct_orientation)
    scanners[scanner_id].orientation = correct_orientation
    displacement = pairs[0][1] - pairs[0][0]
    scanners[scanner_id].translation = displacement
    for beacon in scanners[scanner_id].beacons.values():
        beacon.x += displacement.x
        beacon.y += displacement.y
        beacon.z += displacement.z
    return


# And then we need to do ALL of that until we found each scanner
while len(known_scanners) < len(scanners.keys()):
    locate_scanner()

print()
for scanner in scanners.values():
    print(scanner)
