import math

races_1 = [(49, 263), (97, 1532), (94, 1378), (94, 1851)]
races_2 = [(49979494, 263153213781851)]

winners = []
for race in races_2:
    winner = 0
    for x in range(race[0]):
        distance = x * (race[0]-x)
        if distance > race[1]:
            winner += 1
    winners.append(winner)

print(math.prod(winners))
