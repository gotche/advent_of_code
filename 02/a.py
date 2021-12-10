import sys

# read file
data = sys.stdin.readlines()

# clean
data = [(i.split()[0], int(i.split()[1])) for i in data]

# process
h, depth = 0, 0

for instruction in data:
    match instruction:
        case ('forward', x):
            h += x
        case ('down', x):
            depth += x
        case ('up', x):
            depth -= x

print(h*depth)
