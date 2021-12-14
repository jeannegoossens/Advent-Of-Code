fish = [int(i) for i in open("inputs/day06.txt").read().split(',')]
fish = {i: fish.count(i) for i in range(9)}


def runday(fish):
    fish6 = fish[6]
    fish[6] = fish[7] + fish[0]
    fish[7] = fish[8]
    fish[8] = fish[0]
    fish[0] = fish[1]
    fish[1] = fish[2]
    fish[2] = fish[3]
    fish[3] = fish[4]
    fish[4] = fish[5]
    fish[5] = fish6
    return fish


for i in range(256):
    fish = runday(fish)
print(sum(fish.values()))
