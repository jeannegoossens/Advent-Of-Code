player1, player2 = open('testinput.txt').read().split('\n')
# player1, player2 = open('inputs/day21.txt').read().split('\n')
player1_pos = int(player1.split(": ")[1])
player2_pos = int(player2.split(": ")[1])

d100 = list(range(1,101))

board = [10,1,2,3,4,5,6,7,8,9]


def getposition(current, roll):
    return (current + roll) % 10


def getscore(current, new_position):
    return current + board[new_position]


def rolldie(die_index):
    idx = [die_index%100, (die_index+1)%100, (die_index+2)%100]
    return sum([d100[idx[0]], d100[idx[1]], d100[idx[2]]])


player1_score = 0
player2_score = 0
die_index = 0
turns = 0
player1_turn = True
while player1_score < 1000 and player2_score < 1000:
    roll = rolldie(die_index)
    if player1_turn:
        player1_pos = getposition(player1_pos, roll)
        player1_score = getscore(player1_score, player1_pos)
    else:
        player2_pos = getposition(player2_pos, roll)
        player2_score = getscore(player2_score, player2_pos)
    player1_turn = not player1_turn
    die_index += 3
    turns += 1

print(turns*3)
print(player1_score)
print(player2_score)

print("part 1", min(player1_score, player2_score) * (turns*3))
