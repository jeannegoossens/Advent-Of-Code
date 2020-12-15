input = [11,18,0,20,1,7,16]


# If that was the first time the number has been spoken, the current player says 0.
# Otherwise, the number had been spoken before; the current player announces how many turns apart the number is from when it was previously spoken.


def run_game(end):
    visited = {11: [1],
               18: [2],
               0: [3],
               20: [4],
               1: [5],
               7: [6],
               16: [7]}
    last = 16
    for i in range(8, end+1):
        if len(visited[last]) == 1:
            answer = 0
        else:
            answer = visited[last][-1] - visited[last][-2]
        if answer not in visited.keys():
            visited[answer] = [i]
        else:
            visited[answer].append(i)
        last = answer
    return last


print('solution to part 1:', run_game(2020))
print('solution to part 2:', run_game(30000000))
