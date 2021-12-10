lines = open('input.txt').read().split()
lines = list(filter(None, lines))

print(lines)

metasum = 0
def getNode():
    global metasum
    children = lines.pop(0)
    metadatas = lines.pop(0)
    for child in range(int(children)):
        getNode()
    for metas in range(int(metadatas)):
        metasum += int(lines.pop(0))

getNode()

print(metasum)