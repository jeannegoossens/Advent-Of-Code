import copy

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ROOM_INDEXES = {'A': 2, 'B': 4, 'C': 6, 'D': 8}


class Board:
    def __init__(self, apods):
        self.apods = apods


board = Board()

neighbours = {0: [1],
              1: [0, 2, 'A'],
              2: [1, 3, 'A', 'B'],
              3: [2, 4, 'B', 'C'],
              4: [3, 5, 'C', 'D'],
              5: [4, 6, 'D'],
              6: [5],
              'A': [1, 2],
              'B': [2, 3],
              'C': [3, 4],
              'D': [4, 5]
              }

parking = [0, 1, 3, 5, 7, 9, 10]
taken = []
pods = [('A', ())]

rooms = [['D1', 'D2'], ['A1', 'C1'], ['C2', 'B1'], ['A2', 'B2']]


def is_free(spot):
    return not(spot in taken)


def can_reach(room_index, pod):
    options = []
    for neighbour in neighbours[room_index]:
        if neighbour not in taken:
            if type(neighbour) == 'int':
                options.append(neighbour)
            else:
                if can_leave(room) and is_clear(neighbour, pod):


# determine whether a pod can move into a room
def is_clear(room, pod):
    return len(room) == 0 or (len(room) == 1 and room[0] == pod)


def can_leave(room):
    if len(room) > 0:
        return room[0]
    return None


def find_moves():
    for room in rooms:
        pod = canLeave(room)
        if pod:
            findSpace = freeParking()
