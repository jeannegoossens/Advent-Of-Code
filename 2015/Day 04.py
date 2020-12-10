# 2015
# Day 4

import hashlib

input = """iwrupvqb"""

result = ''
count = 1

while result[:6] != '000000':
    x = input + str(count)
    result = hashlib.md5(x.encode()).hexdigest()
    count += 1

print(count -1)