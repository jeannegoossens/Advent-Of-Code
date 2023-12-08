inp = open('inputs/Day03.txt').read().split('\n')

print(inp)

# 467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598..

inp = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..""".split('\n')

circle = [(-1,-1), (-1,0), (-1,1),
          (0,-1), (0,1),
          (1,-1), (1,0), (1,1)]

numbers = []

for row in range(len(inp)):
    column = 0
    while column < len(inp[row]):
        if inp[row][column].isnumeric():
            if inp[row][column+1].isnumeric():
                if column+2 < len(inp[row]) and inp[row][column+2].isnumeric():
                    number = inp[row][column:column+3]
                    numbers.append(number)
                    column += 3
                    continue
                else:
                    number = inp[row][column:column+2]
                    numbers.append(number)
                    column += 2
                    continue
            else:
                number = inp[row][column]
                numbers.append(number)
                column += 1
                continue
        column += 1

print(numbers)
