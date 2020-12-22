input = open('inp.txt').read().split('\n')
import re

input = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".split('\n')


for line in input:
    alls = [y for x in re.findall(r' \(contains (.*)\)', line) for y in x.split(', ')]
    ings = line.split(' (')[0].split(' ')
