inp = '916438275'
testinp = '389125467'

# circular linked list method
# see commit history on this file for a string manipulation method used for part 1


class Cup:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Circle:
    def __init__(self):
        self.cups = {}

    def add_after(self, value, cup=None) -> Cup:
        newCup = Cup(value)

        if cup is None:
            newCup.next = newCup
            newCup.prev = newCup
        else:
            newCup.next = cup.next
            newCup.prev = cup
            cup.next = newCup
            newCup.next.prev = newCup

        self.cups[value] = newCup

        return newCup

    def remove_after(self, currentCup) -> int:
        pickedCup = currentCup.next
        currentCup.next = pickedCup.next
        currentCup.next.prev = currentCup

        cupValue = pickedCup.value

        del self.cups[cupValue]
        del pickedCup

        return cupValue

    def find(self, value) -> Cup:
        return self.cups[value]


# fill the circle
inp = [int(i) for i in inp]
circle = Circle()
lastCup = None
for i in list(inp):
    lastCup = circle.add_after(i, lastCup)
for i in range(max(list(inp)) + 1, 1000001):
    lastCup = circle.add_after(i, lastCup)

# do the turns
currentCup = circle.find(inp[0])
for move in range(10000000):
    cup1 = circle.remove_after(currentCup)
    cup2 = circle.remove_after(currentCup)
    cup3 = circle.remove_after(currentCup)

    if currentCup.value == 1:
        destinationCup = 1000000
    else:
        destinationCup = currentCup.value - 1
    while destinationCup in [cup1, cup2, cup3]:
        if destinationCup == 1:
            destinationCup = 1000000
        else:
            destinationCup -= 1

    for cup in [cup3, cup2, cup1]:
        circle.add_after(cup, circle.find(destinationCup))

    currentCup = currentCup.next

print(circle.find(1).next.value * circle.find(1).next.next.value)
