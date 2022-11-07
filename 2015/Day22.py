spells = [
    {'mana': 53, 'effect': 'instant', 'damage': 4},
    {'mana': 73, 'effect': 'instant', 'damage': 2, 'heal': 2},
    {'mana': 113, 'effect': 6, 'armor': 7},
    {'mana': 173, 'effect': 6, 'damage': 3},
    {'mana': 229, 'effect': 5, 'gain': 101}
]

me = {'mana': 500, 'hp': 50}
boss = {'hp': 58, 'damage': 9}


def battle(me):
    boss = {'hp': 58, 'damage': 9}
    myturn = True
    while me['Hit Points'] > 0 and boss['Hit Points'] > 0:
        if myturn:
            boss['Hit Points'] -= max(1, me['Damage'] - boss['Armor'])
        else:
            me['Hit Points'] -= max(1, boss['Damage'] - me['Armor'])
        myturn = not myturn
    return me['Hit Points'] > 0 and boss['Hit Points'] <= 0