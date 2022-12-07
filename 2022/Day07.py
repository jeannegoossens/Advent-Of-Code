inp = open('inputs/Day07.txt').read().split('\n')

# track our path, for there are nested dirs with similar names
prevdir = []  # parent dirs
curdir = ''  # current dir
sizes = {'': 0}


def getpath(prevdir, curdir):
    # the path to a dir consists of all parent dirs
    if len(prevdir) > 0:
        path = '/'.join(prevdir) + '/' + curdir
    else:
        path = curdir
    return path


# count the total sizes for each dir
for line in inp:
    # get the full path to the current dir
    path = getpath(prevdir, curdir)

    # now parse the line
    if line == '$ cd /':
        # go back to home dir
        prevdir = []
        curdir = ''

    elif line == '$ cd ..':
        # go one step back
        curdir = prevdir.pop()

    elif line.startswith('$ cd'):
        # step into dir
        prevdir.append(curdir)
        curdir = line.split()[2]

    elif line.split()[0].isnumeric():
        # this is a line with a file size
        for topdir in range(len(prevdir)):
            # for each parent directory increase the size with the found file size
            sizes[getpath(prevdir[:topdir], prevdir[topdir])] += int(line.split()[0])
        # and increase the current dir with the file size
        sizes[path] += int(line.split()[0])

    elif line.startswith('dir'):
        # this is a line with a dir name
        if len(prevdir) > 0:
            dirpath = path + '/' + line.split()[1]
        else:
            dirpath = curdir + '/' + line.split()[1]
        sizes[dirpath] = 0

    # the other line types don't matter

# now get the sum of the small dirs
total = sum([v for v in sizes.values() if v <= 100_000])
print("part 1:", total)

# and get the smallest dir to remove that frees up enough space
spacetofree = 30_000_000 - (70_000_000 - sizes[''])
s = [v for k, v in sorted(sizes.items(), key=lambda item: item[1]) if v > spacetofree]
print("part 2:", s[0])
