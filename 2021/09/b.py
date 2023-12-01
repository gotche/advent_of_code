import sys

# read file
data = sys.stdin.readlines()

# clean
data = [list(i.strip()) for i in data]

minimums = []
positions = []

for i, line in enumerate(data):
    for j, value in enumerate(line):
        minimum = []

        if i > 0:
            minimum.append(value < data[i - 1][j])

        if i < len(data) - 1:
            minimum.append(value < data[i + 1][j])

        if j > 0:
            minimum.append(value < line[j - 1])

        if j < len(line) - 1:
            minimum.append(value < line[j + 1])

        if all(minimum):
            minimums.append(value)
            positions.append((i, j))


def find_basin(i, j, results):
    if i < 0 or i > len(data) - 1 or j < 0 or j > len(data[0]) - 1:
        return
    if data[i][j] == "9":
        return
    if (i, j) not in results:
        results.add((i, j))
        find_basin(i - 1, j, results)
        find_basin(i + 1, j, results)
        find_basin(i, j - 1, results)
        find_basin(i, j + 1, results)


results = []
for position in positions:
    result = set()
    find_basin(*position, result)
    results.append(result)

length = sorted(len(i) for i in results)
print(length[-1] * length[-2] * length[-3])
