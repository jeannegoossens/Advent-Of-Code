shop = {
    'Weapons': [
        {'Damage': 4, 'Cost': 8},
        {'Damage': 5, 'Cost': 10},
        {'Damage': 6, 'Cost': 25},
        {'Damage': 7, 'Cost': 40},
        {'Damage': 8, 'Cost': 74}
    ],
    'Armor': [
        {'Armor': 0, 'Cost': 0},
        {'Armor': 1, 'Cost': 13},
        {'Armor': 2, 'Cost': 31},
        {'Armor': 3, 'Cost': 53},
        {'Armor': 4, 'Cost': 75},
        {'Armor': 5, 'Cost': 102}
    ],
    'Rings': [
        {'Damage': 0, 'Armor': 0, 'Cost': 0},
        {'Damage': 0, 'Armor': 0, 'Cost': 0},
        {'Damage': 1, 'Armor': 0, 'Cost': 25},
        {'Damage': 2, 'Armor': 0, 'Cost': 50},
        {'Damage': 3, 'Armor': 0, 'Cost': 100},
        {'Damage': 0, 'Armor': 1, 'Cost': 20},
        {'Damage': 0, 'Armor': 2, 'Cost': 40},
        {'Damage': 0, 'Armor': 3, 'Cost': 80}
    ]
}


def battle(me):
    boss = {
        'Hit Points': 100,
        'Damage': 8,
        'Armor': 2
    }
    myturn = True
    while me['Hit Points'] > 0 and boss['Hit Points'] > 0:
        if myturn:
            boss['Hit Points'] -= max(1, me['Damage'] - boss['Armor'])
        else:
            me['Hit Points'] -= max(1, boss['Damage'] - me['Armor'])
        myturn = not myturn
    return me['Hit Points'] > 0 and boss['Hit Points'] <= 0


maxcost = 0
mincost = 500
for w in shop['Weapons']:
    for a in shop['Armor']:
        for r1 in range(len(shop['Rings'])):
            for r2 in range(len(shop['Rings'])):
                if r1 != r2:
                    me = {
                        'Hit Points': 100,
                        'Damage': w['Damage'] + shop['Rings'][r1]['Damage'] + shop['Rings'][r2]['Damage'],
                        'Armor': a['Armor'] + shop['Rings'][r1]['Armor'] + shop['Rings'][r2]['Armor']
                    }
                    cost = w['Cost'] + a['Cost'] + shop['Rings'][r1]['Cost'] + shop['Rings'][r2]['Cost']
                    if not battle(me):
                        maxcost = max(cost, maxcost)
                    else:
                        mincost = min(cost, mincost)

print(mincost)
print(maxcost)
