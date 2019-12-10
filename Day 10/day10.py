class Asteroid():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vectors = []
        self.visible = 0
    
    def __sub__(self, other):
        subx = self.x - other.x
        suby = self.y - other.y
        return (subx, suby)
    
    def __repr__(self):
        return 'Asteroid located on coordinates {x: %s, y: %s} detects %s others' % (self.x, self.y, self.visible)
    
    def setVector(self, other):
        vector = self - other
        # simplify these vectors so i can compare them
        try:  # catch div by 0
            vector = (vector[0]/abs(vector[0]), vector[1]/abs(vector[0]))
        except: pass
        self.vectors.append(vector)
        
        # asteroids that are behind each other will have the same vector
        # e.g. (2,4) is behind (1,2)
        self.visible = len(list(set(self.vectors)))
        

astmap = open('input.txt').read().split('\n')

# get a list of all the asteroids in the map, and their coordinates
asteroids = []
for line in range(len(example)):
    for c in range(len(example[line])):
        if example[line][c] == '#':
            a = Asteroid(c, line)
            asteroids.append(a)

# for every asteroid, get the vector direction to all other asteroids
for a in asteroids:
    for b in asteroids:
        if a != b:
            a.setVector(b)

# get the highest amount of detected asteroids
maxim = 0
for a in asteroids:
    maxim = max(maxim, a.visible)
    if a.visible >= maxim:
        print(a)
print(maxim)
