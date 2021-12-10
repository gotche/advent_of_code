import sys

# read file
data = sys.stdin.readlines()

# clean
data = [(i.split()[0], int(i.split()[1])) for i in data]

# process
h, depth, aim = 0, 0, 0

for instruction in data:
    match instruction:
        case ('forward', x):
            h += x
            depth += aim * x
        case ('down', x):
            aim += x
        case ('up', x):
            aim -= x

print(h*depth)
