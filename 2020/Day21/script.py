# each allergen is found in exactly 1 ingredient
# each ingredient contains 0 or 1 allergen
# allergens are not always marked

recipes = open('testinput.txt').read().split('\n')
recipes = [[x.split(' (contains ')[0], x.split(' (contains ')[1].strip(')')] for x in recipes]
recipes = [{'ingredients': sorted(x[0].split(' ')), 'allergens':  x[1].split(', ')} for x in recipes]

all_allergens = set([item for a in recipes for item in a['allergens']])
all_ingredients = set([item for i in recipes for item in i['ingredients']])

possible_ingredients = {a: set() for a in all_allergens}

for a in all_allergens:
    for recipe in recipes:
        if a in recipe['allergens']:
            possible_ingredients[a].update(recipe['ingredients'])


# safe: kfcds, nhms, sbzzf, trh
