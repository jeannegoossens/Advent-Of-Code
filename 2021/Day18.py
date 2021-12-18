import re
import ast

inp = open('inputs/day18.txt').read().split('\n')


def add(cluster1, cluster2):
    cluster = '[' + cluster1 + ',' + cluster2 + ']'
    return cluster


def explode(cluster, pair, start, end):
    numbers = re.finditer(r'[0-9]{1,2}', cluster)
    numbers = [i for i in numbers]

    previous = [[int(i.group()), i.start(), i.end()] for i in numbers if i.start() < start]
    if len(previous) > 0:
        previous = previous[-1]

    next = [[int(i.group()), i.start(), i.end()] for i in numbers if i.start() > end]
    if len(next) > 0:
        next = next[0]

    pairlist = ast.literal_eval(pair)
    if len(previous) > 0:
        first = pairlist[0] + previous[0]
        cluster = cluster[:previous[1]] + str(first) + cluster[previous[2]:]
    else:
        first = 0
    if len(next) > 0:
        second = pairlist[1] + next[0]
        if first >= 10 and previous[0] < 10:
            cluster = cluster[:next[1]+1] + str(second) + cluster[next[2]+1:]
        else:
            cluster = cluster[:next[1]] + str(second) + cluster[next[2]:]
    if first >= 10 and previous[0] < 10:
        newcluster = cluster[:start+1] + '0' + cluster[end+1:]
    else:
        newcluster = cluster[:start] + '0' + cluster[end:]
    return newcluster


def splitcluster(cluster, greatnumber):
    first = int(int(greatnumber.group())/2)
    second = int((int(greatnumber.group())+1)/2)
    cluster = cluster[:greatnumber.start()] + '[' + str(first) + ',' + str(second) + ']' + cluster[greatnumber.end():]
    return cluster


def reduce(cluster):
    pairs = re.finditer(r'\[[0-9]{1,2},[0-9]{1,2}\]', cluster)
    newcluster = ''.join([i for i in cluster])
    if pairs:
        pairs = [p for p in pairs]
        if len(pairs) > 0:
            for regexpair in pairs:
                pair = regexpair.group()
                start_index = regexpair.start()
                end_index = regexpair.end()
                if cluster[:start_index].count('[') - cluster[:start_index].count(']') == 4:
                    newcluster = explode(cluster, pair, start_index, end_index)
                    break
    if newcluster == cluster:
        greater = re.finditer(r'[0-9]{2}', newcluster)
        if greater:
            greater = [g for g in greater]
            if len(greater) > 0:
                greatnumber = [g for g in greater][0]
                newcluster = splitcluster(cluster, greatnumber)
    return newcluster


def calcmagnitude(cluster):
    inner = re.search(r'\[[^\]\[]*\]', cluster)
    numbers = [i for i in re.finditer(r'[0-9]{1,}', inner.group())]
    solution = int(numbers[0].group())*3 + int(numbers[1].group())*2
    cluster = cluster.replace(inner.group(), str(solution))
    return cluster


def getmagnitude(cluster):
    while not cluster.isnumeric():
        cluster = calcmagnitude(cluster)
    return int(cluster)


def runCluster(clusters):
    newcluster = '0'
    cluster = clusters[0]
    for number in clusters[1:]:
        cluster = add(cluster, number)
        newcluster = reduce(cluster)
        while cluster != newcluster:
            cluster = newcluster
            newcluster = reduce(cluster)
    return getmagnitude(newcluster)


print('part 1:', runCluster(inp))
# part 1: 3699

maxmagnitude = 0
for i in range(len(inp)):
    for j in range(len(inp)):
        if i != j:
            c = [inp[i], inp[j]]
            maxmagnitude = max(maxmagnitude, runCluster(c))

print('part 2:', maxmagnitude)
# part 2 4735
