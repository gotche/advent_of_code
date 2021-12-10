import sys

# read file
data = sys.stdin.readlines()

# clean
data = [int(i) for i in data[0].split(",")]

# process
data.sort()
index = len(data) // 2
avg = round(sum(data) / len(data))

count = 0
for i in data:
    value = abs(i - avg)
    count += value * (value + 1) * (1 / 2)

count1 = 0
for i in data:
    value = abs(i - avg - 1)
    count1 += value * (value + 1) * (1 / 2)

count2 = 0
for i in data:
    value = abs(i - avg + 1)
    count2 += value * (value + 1) * (1 / 2)
print(int(min(count, count1, count2)))
