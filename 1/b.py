import sys

# read file
data = sys.stdin.readlines()

# clean
data = [int(i) for i in data]


# process
counter = 0

for i in range(len(data) - 3):
    if data[i + 3] > data[i]:
        counter += 1

print(counter)
