import re

inp = open('inputs/Day16.txt').read().split('\n')

valves = {}

for line in inp:
    thesevalves = re.findall('[A-Z]{2}', line)
    flowrate = int(re.findall('[0-9]{1,2}', line)[0])
    valves[thesevalves[0]] = {'flow': flowrate, 'connections': thesevalves[1:]}

for k, v in valves.items():
    print(k, v)

source = 'AA'
dist = {v: 100_000_000 for v in valves.keys()}
prev = {v: None for v in valves.keys()}
queue = [v for v in valves.keys()]
dist[source] = 0


