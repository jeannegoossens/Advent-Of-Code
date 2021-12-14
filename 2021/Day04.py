import re
inp = open("inputs/day04.txt").read().split('\n\n')


def makeBoard(board):
    b = {}
    for y in range(len(board)):
        row = board[y].strip().replace(r'  ', ' ').split(' ')
        for x in range(len(row)):
            field = row[x]
            if len(field) > 0:
                b[int(field)] = {'value': False, 'coordinates': (y,x)}
    return b


def checkBingo(board, call):
    cs = board[call]['coordinates']
    # check row
    row = True
    column = True
    for k, v in board.items():
        if v['coordinates'][1] == cs[1]:
            if v['value'] == False:
                row = False
        if v['coordinates'][0] == cs[0]:
            if v['value'] == False:
                column = False
    if row == False and column == False:
        return False
    else:
        return True


def checkBingo(board, call):
    cs = board[call]['coordinates']
    # check row
    row = True
    column = True
    for k, v in board.items():
        if v['coordinates'][1] == cs[1]:
            if v['value'] == False:
                row = False
        if v['coordinates'][0] == cs[0]:
            if v['value'] == False:
                column = False
    if row == False and column == False:
        return False
    else:
        return True


def getscore(board, lastcall):
    sum = 0
    for k, v in board.items():
        if v['value'] == False:
            sum += k
    print(sum)
    return sum * lastcall


def play_game(calls, boards):
    wins = []
    for call in calls:
        for b in range(len(boards)):
            board = boards[b]
            if call in board.keys():
                board[call]['value'] = True
                if checkBingo(board, call):
                    if board not in wins:
                        wins.append(board)
                    if len(wins) > len(boards)-1:
                        return b, call


calls = [int(i) for i in inp[0].split(',')]
boards = [board.split('\n') for board in inp[1:]]
boards = [makeBoard(board) for board in boards]
boardindex, call = play_game(calls, boards)
print(getscore(boards[boardindex], call))

# 11774 part 1
# 4495 part 2
