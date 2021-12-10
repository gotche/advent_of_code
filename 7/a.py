import sys

# read file
data = sys.stdin.readlines()

# clean
data = [int(i) for i in data[0].split(",")]

# process
data.sort()
print(data)
index = len(data) // 2
print(index)
print(data[index])

print(sum(abs(i - data[index]) for i in data))
