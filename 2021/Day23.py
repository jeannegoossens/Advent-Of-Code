import copy

COST = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
ROOM_INDEXES = {'A': 2, 'B': 4, 'C': 6, 'D': 8}


class Board:
    def __init__(self, hallway, rooms):
        self.hallway = hallway
        self.rooms = rooms

    def __repr__(self):
        return f"{[str(i) for i in range(11)]}\n{self.hallway}, {self.rooms}"

    def __hash__(self):
        return hash(f"{self.hallway}, {self.rooms}")

    def __copy__(self):
        return Board([i for i in self.hallway], {r: p for r, p in self.rooms.items()})


def is_finished(board):
    for room, amphipods in board.rooms.items():
        for amphipod in amphipods:
            if amphipod != room:
                return False
    return True


def can_leave_room(room, board):
    for amphipod in board.rooms[room]:
        if amphipod != room and amphipod != '.':
            return True
    return False


def first_empty_room_space(room, board):
    for index, amphipod in reversed(list(enumerate(board.rooms[room]))):
        if amphipod == '.':
            return index
    return None


def first_filled_room_space(room, board):
    for index, amphipod in enumerate(board.rooms[room]):
        if amphipod != '.':
            return index
    return None


def can_go_home(amphipod, board):
    if len([pod for pod in board.rooms[amphipod] if pod == amphipod]) == len(board.rooms[amphipod]):
        return False
    # can go home if there's not hostile pods in this room
    for hostile in board.rooms[amphipod]:
        if hostile != amphipod and hostile != '.':
            return False
    return True


def hallway_not_obstructed(start, destination, board):
    if start < destination:
        start += 1
    elif start > destination:
        start -= 1
    for field in board.hallway[min(start, destination):max(start, destination)+1]:
        if field != '.':
            return False
    return True


# would be too much (uninteresting) code and time to parse the input file to this data, so dit it manually
board = Board(['.' for _ in range(11)], {'A': ['D', 'D'], 'B': ['A', 'C'], 'C': ['C', 'B'], 'D': ['A', 'B']})
memo = {}


def move(board):
    if is_finished(board):
        return 0
    if board in memo.keys():
        return memo[board]
    # first clear the hallway space as much as possible
    for index, field in enumerate(board.hallway):
        if field != '.':
            amphipod = field
            if can_go_home(amphipod, board):
                if hallway_not_obstructed(index, ROOM_INDEXES[amphipod], board):
                    distance = abs(index - ROOM_INDEXES[amphipod]) + 1
                    new_board = copy.copy(board)
                    new_board.hallway[index] = '.'
                    new_board.rooms[amphipod][first_empty_room_space(amphipod, board)] = amphipod
                    cost = distance * COST[amphipod] + move(new_board)
                    return cost
    # otherwise move a pod from its room
    mincost = 1_000_000_000
    for room, amphipods in board.rooms.items():
        pod_index = first_filled_room_space(room, board)
        if pod_index and can_leave_room(room, board):
            amphipod = room[pod_index]
            for index, field in enumerate(board.hallway):
                if hallway_not_obstructed(ROOM_INDEXES[room], index, board):
                    distance = abs(index - ROOM_INDEXES[room]) + 1
                    new_board = copy.copy(board)
                    new_board.hallway[index] = amphipod
                    new_board.rooms[room] = '.'
                    cost = distance * COST[amphipod] + move(new_board)
                    mincost = min(mincost, cost)
    return mincost


print(move(board))
