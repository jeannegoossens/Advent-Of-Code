inp = list(open('inputs/Day17.txt').read())

jets = inp

blocks = [
    [(0, 0), (0, 1), (0, 2), (0, 3)],  # horizontal line
    [(0, 1), (1, 0), (1, 1), (1, 2), (2, 1)],  # cross
    [(0, 2), (1, 2), (2, 0), (2, 1), (2, 2)],  # corner
    [(0, 0), (1, 0), (2, 0), (3, 0)],  # vertical line
    [(0, 0), (0, 1), (1, 0), (1, 1)]  # cube
]

board = []

jetidx = 0
blockidx = 0

for rock in range(2022):
    settled = False
    block = blocks[blockidx]
    
