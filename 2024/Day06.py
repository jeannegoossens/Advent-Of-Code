inp = open('inputs/Day06.txt').read()
grid = inp.split('\n')

guard = (int(inp.find("^") / len(grid) - 1), grid[int(inp.find("^") / len(grid)) -1].find("^"))
direction = "^"
grid[guard[0]] = grid[guard[0]].replace('^', '.')
original_guard_position = guard

passed = set()
potentials = set()

while 0 <= guard[0] < len(grid) and 0 <= guard[1] < len(grid[0]):
    if guard in passed and guard != original_guard_position:
        potentials.add(guard)
    else:
        passed.add(guard)
    if direction == "^":
        if grid[guard[0]-1][guard[1]] == '.':
            guard = (guard[0]-1, guard[1])
        elif grid[guard[0]-1][guard[1]] == '#':
            direction = ">"
    elif direction == ">":
        if grid[guard[0]][guard[1]+1] == '.':
            guard = (guard[0], guard[1]+1)
        elif grid[guard[0]][guard[1]+1] == '#':
            direction = "v"
    elif direction == "v":
        if guard[0]+1 >= len(grid) or grid[guard[0]+1][guard[1]] == '.':
            guard = (guard[0]+1, guard[1])
        elif grid[guard[0]+1][guard[1]] == '#':
            direction = "<"
    elif direction == "<":
        if grid[guard[0]][guard[1]-1] == '.':
            guard = (guard[0], guard[1]-1)
        elif grid[guard[0]][guard[1]-1] == '#':
            direction = "^"

print("Part 1:", len(passed))
print("Part 2:", len(potentials))  # 761 too low
