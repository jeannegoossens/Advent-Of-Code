row = 2947
column = 3029
multiply = 252533
divide = 33554393
code = 20151125

nr = int((column + 1) * (column / 2))
step = column
for i in range(1, row):
    nr += step
    step += 1

print('the right code is at index number:', nr)

for x in range(nr-1):
    code = (code * multiply) % divide

print('the right code is:', code)