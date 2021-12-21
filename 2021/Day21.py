player1, player2 = open('inputs/day21.txt').read().split('\n')

player1_pos = int(player1.split(": ")[1])  # 4
player2_pos = int(player2.split(": ")[1])  # 8

player1_score = 0
player2_score = 0

board = [10, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def getposition(current, roll):
    return (current + roll) % 10


def getscore(current, new_position):
    return current + board[new_position]


def playgame(curr_pos, curr_score, other_pos, other_score):
    if curr_score >= 21:  # current player wins
        return (1, 0)
    if other_score >= 21:  # other player wins
        return (0, 1)

    # have we seen this situation before
    if (curr_pos, curr_score, other_pos, other_score) in memo:
        return memo[(curr_pos, curr_score, other_pos, other_score)]

    # we have not so roll the dice
    wins = (0,0)
    for roll1 in [1, 2, 3]:
        for roll2 in [1, 2, 3]:
            for roll3 in [1, 2, 3]:
                new_pos = getposition(curr_pos, sum([roll1, roll2, roll3]))
                new_score = getscore(curr_score, new_pos)
                # now get the amount of wins for each player,
                # and set the current player to the other player
                other_wins, curr_wins = playgame(other_pos, other_score, new_pos, new_score)
                # add the results to the right players
                wins = (wins[0] + curr_wins, wins[1] + other_wins)
    # now store this new result to memorized situations
    memo[(curr_pos, curr_score, other_pos, other_score)] = wins
    return wins


memo = {}
total_wins = playgame(player1_pos, player1_score, player2_pos, player2_score)
print("part 2", max(total_wins))

# part 1: 713328
# part 2: 92399285032143
