import sys

# read file
data = sys.stdin.readlines()

# clean
data = [list(i.strip()) for i in data]

print(data)

minimums = []

for line_index, line in enumerate(data):
    minimum = []
    for i in range(len(line)):
        if line_index > 0:
            minimum.append(line[i] < data[line_index - 1][i])

        if line_index < len(data) - 1:
            minimum.append(line[i] < data[line_index + 1][i])

        if i > 0:
            minimum.append(line[i] < line[i - 1])

        if i < len(line) - 1:
            minimum.append(line[i] < line[i + 1])

        if all(minimum):
            minimums.append(line[i])
        minimum = []

risk = sum(int(i) for i in minimums) + len(minimums)
print(risk)
