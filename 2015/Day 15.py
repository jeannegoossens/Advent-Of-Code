# 2015
# Day 15

inp = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""
inp = inp.split('\n')
inp = {i.split(': ')[0]: {j.split(' ')[0]: j.split(' ')[1] for j in i.split(': ')[1].split(', ')} for i in inp}

combinations = []
for a in range(1,101):
    for b in range(1,101):
        for c in range(1,101):
            for d in range(1,101):
                if sum([a,b,c,d]) == 100:
                    combinations.append([a,b,c,d])

maxscore = 0
for c in combinations:
    capacity = 0
    durability = 0
    flavor = 0
    texture = 0
    calories = 0
    inp['Frosting']['amount'] = c[0]
    inp['Candy']['amount'] = c[1]
    inp['Butterscotch']['amount'] = c[2]
    inp['Sugar']['amount'] = c[3]
    for ingredient in inp.keys():
        capacity += int(inp[ingredient]['capacity']) * inp[ingredient]['amount']
        durability += int(inp[ingredient]['durability']) * inp[ingredient]['amount']
        flavor += int(inp[ingredient]['flavor']) * inp[ingredient]['amount']
        texture += int(inp[ingredient]['texture']) * inp[ingredient]['amount']
        calories += int(inp[ingredient]['calories']) * inp[ingredient]['amount']
    if calories != 500:
        continue
    score = max(0, capacity) * max(0, durability) * max(0, flavor) * max(0, texture)
    maxscore = max(maxscore, score)
        
print(maxscore)
