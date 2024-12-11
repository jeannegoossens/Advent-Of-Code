inp = [int(i) for i in open('inputs/Day11.txt').read().split()]

mapping = {i: inp.count(i) for i in inp}


def generation(mapping):
    new = {}
    for key, value in mapping.items():
        if key == 0:
            if 1 in new.keys():
                new[1] += value
            else:
                new[1] = value
        elif len(str(key)) % 2 == 0:
            half = int(len(str(key)) / 2)
            left = int(str(key)[:half])
            right = int(str(key)[half:])
            if left in new.keys():
                new[left] += value
            else:
                new[left] = value
            if right in new.keys():
                new[right] += value
            else:
                new[right] = value
        else:
            if key * 2024 in new.keys():
                new[key * 2024] += value
            else:
                new[key * 2024] = value
    return new


for i in range(25):
    mapping = generation(mapping)

print("part 1:", sum(mapping.values()))

for i in range(50):
    mapping = generation(mapping)

print("part 2:", sum(mapping.values()))
