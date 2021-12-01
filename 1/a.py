import sys

# read file
data = sys.stdin.readlines()

# clean
data = [int(i) for i in data]


# process
data = iter(data)

counter = 0
last = next(data)

for i in data:
    if i > last:
        counter += 1
    last = i

print(counter)
