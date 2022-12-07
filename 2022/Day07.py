inp = open('inputs/Day07.txt').read().split('\n')

directories = {'': {}}

# track our path, for there are nested dirs with similar names
prevdir = []
curdir = ''

# deduct the file system
for line in inp:
    if len(prevdir) > 0:
        path = '/'.join(prevdir) + '/' + curdir
    else:
        path = curdir
    if line == '$ cd /':
        prevdir = []
        curdir = ''
    elif line == '$ ls':
        continue
    elif line == '$ cd ..':
        curdir = prevdir.pop()
    elif line.startswith('$ cd'):
        prevdir.append(curdir)
        curdir = line.split()[2]
    elif line.split()[0].isnumeric():
        directories[path][line.split()[1]] = int(line.split()[0])
    elif line.startswith('dir'):
        if len(prevdir) > 0:
            dirpath = '/'.join(prevdir) +'/' + curdir + '/' + line.split()[1]
        else:
            dirpath = curdir + '/' + line.split()[1]
        directories[path][dirpath] = 'dir'
        directories[dirpath] = {}

sizes = {k: 0 for k in directories.keys()}


# recursively count the size of each dir
def dive(curdir):
    global sizes
    dirsum = 0
    for key, content in directories[curdir].items():
        if type(content) == int:
            dirsum += content
        else:
            dirsum += dive(key)

    sizes[curdir] += dirsum
    return dirsum


# print the file system in a neat format
def printdir(dir, level):
    for k, v in directories[dir].items():
        if v == 'dir':
            print('  ' * level, v, k, sizes[k])
            printdir(k, level + 1)
        else:
            print('  ' * level, k, v)
    return


dive('')

total = sum([v for v in sizes.values() if v <= 100_000])
print("part 1:", total)

maxsize = 70_000_000
freespace = maxsize - sizes['']
s = [v for k, v in sorted(sizes.items(), key=lambda item: item[1]) if v > 30_000_000 - freespace]
print("part 2:", s[0])
