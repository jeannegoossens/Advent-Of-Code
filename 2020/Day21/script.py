recipes = open('input.txt').read().split('\n')
recipes = [[x.split(' (contains ')[0], x.split(' (contains ')[1].strip(')')] for x in recipes]
recipes = [{'ingredients': sorted(x[0].split(' ')), 'allergens': x[1].split(', ')} for x in recipes]

all_allergens = set([item for a in recipes for item in a['allergens']])
all_ingredients = set([item for i in recipes for item in i['ingredients']])

allergen_recipes = {a: [] for a in all_allergens}
possible_ingredients = {a: set() for a in all_allergens}
for a in all_allergens:
    for recipe in recipes:
        if a in recipe['allergens']:
            allergen_recipes[a].append(recipe['ingredients'])
            possible_ingredients[a].update(recipe['ingredients'])

possible_allergens = {i: set() for i in all_ingredients}
for i in all_ingredients:
    for recipe in recipes:
        if i in recipe['ingredients']:
            possible_allergens[i].update(recipe['allergens'])

safe_ingredients = []
# for every allergen
for a, a_recipes in allergen_recipes.items():
    # for every ingredient in the possibilities
    for ingredient in possible_ingredients[a]:
        # for every recipe in which this ingredient appears
        for recipe in a_recipes:
            # if the ingredient is not in all of those
            if ingredient not in recipe and a in possible_allergens[ingredient]:
                # it cannot be that ingredient
                possible_allergens[ingredient].remove(a)
safe_ingredients = [i for i, a in possible_allergens.items() if len(a) == 0]

# in how many recipes do these occur?
count = 0
for recipe in recipes:
    for i in safe_ingredients:
        if i in recipe['ingredients']:
            count += 1
print("Part 1:", count)

possible_allergens = {i: a for i, a in possible_allergens.items() if len(a) > 0}
unknown = list(all_ingredients - set(safe_ingredients))
matches = {}

while len(unknown) > 0:
    for ingredient in possible_allergens.keys():
        options = possible_allergens[ingredient]
        if len(options) == 1:
            matches[ingredient] = options.pop()
            unknown.pop(unknown.index(ingredient))

            # also remove it from all other ingredients
            for k, v in possible_allergens.items():
                if matches[ingredient] in v:
                    v.remove(matches[ingredient])
            del possible_allergens[ingredient]
            break

matches = dict(sorted(matches.items(), key=lambda item: item[1]))

print("Part 2:", ','.join([k for k in matches.keys()]))
