# 2015
# Day 15

input = """Frosting: capacity 4, durability -2, flavor 0, texture 0, calories 5
Candy: capacity 0, durability 5, flavor -1, texture 0, calories 8
Butterscotch: capacity -1, durability 0, flavor 5, texture 0, calories 6
Sugar: capacity 0, durability 0, flavor -2, texture 2, calories 1"""

ingredients = {}

for x in input.split('\n'):
   y = x.replace(':', '').replace(',', '').split(' ')
   ingredient = {'capacity': y[2], 'durability': y[4], 'flavor': y[6], 'texture': y[8], 'calories': y[10]}
   ingredients[y[0]] = ingredient

print(ingredients)


def getScore(ingredients, distribution):
    capacity = ingredients['Frosting']['capacity'] * distribution[0] + ingredients['Candy']['capacity'] * distribution[
        0] + ingredients['Butterscotch']['capacity'] * distribution[0] + ingredients['Sugar']['capacity'] * \
               distribution[0]
    durability = ingredients['Frosting']['durability'] * distribution[0] + ingredients['Candy']['durability'] * \
                 distribution[0] + ingredients['Butterscotch']['durability'] * distribution[0] + ingredients['Sugar'][
                     'durability'] * distribution[0]
    flavor = ingredients['Frosting']['flavor'] * distribution[0] + ingredients['Candy']['flavor'] * distribution[0] + \
             ingredients['Butterscotch']['flavor'] * distribution[0] + ingredients['Sugar']['flavor'] * distribution[0]
    texture = ingredients['Frosting']['texture'] * distribution[0] + ingredients['Candy']['texture'] * distribution[0] + \
              ingredients['Butterscotch']['texture'] * distribution[0] + ingredients['Sugar']['texture'] * distribution[
                  0]
    # calories = ingredients['Frosting']['capacity']*distribution[0] + ingredients['Candy']['capacity']*distribution[0] + ingredients['Butterscotch']['capacity']*distribution[0] + ingredients['Sugar']['capacity']*distribution[0]

    score = capacity * durability * flavor * texture
    return score


distribution = [100,0,0,0]
maxScore = 0

for x in range(100000000):
    maxScore = max(maxScore, getScore(ingredients, distribution))
    distribution[0] -= 1
    distribution[1] += 1

    # ??????