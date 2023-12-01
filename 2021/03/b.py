import sys
from copy import deepcopy

# read file
data = sys.stdin.readlines()

# clean
data = [[int(i.strip()) for i in line.strip()] for line in data]

# process


def most_common(data, column):
    ones, zeros = 0, 0
    for line in data:
        if line[column] == 0:
            zeros += 1
        else:
            ones += 1

    if ones >= zeros:
        return 1
    else:
        return 0


co2, o2 = 0, 0
o2_data = deepcopy(data)
co2_data = deepcopy(data)

for col in range(len(data[0])):
    filter_by = most_common(o2_data, col)
    o2_data = [value for value in o2_data if value[col] == filter_by]
    if len(o2_data) == 1:
        break

for col in range(len(data[0])):
    filter_by = most_common(co2_data, col)
    co2_data = [value for value in co2_data if value[col] != filter_by]
    if len(co2_data) == 1:
        break

o2_data = "".join([str(i) for i in o2_data[0]])
co2_data = "".join([str(i) for i in co2_data[0]])

o2 = int(o2_data, base=2)
co2 = int(co2_data, base=2)

print(o2 * co2)
