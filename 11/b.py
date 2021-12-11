import sys

# read file
data = sys.stdin.readlines()

# clean
data = [[int(j) for j in i.strip()] for i in data]


def neighbours(i, j, data):
    maxj = len(data)
    maxi = len(data[0])

    for kj in (j - 1, j, j + 1):
        for ki in (i - 1, i, i + 1):
            if 0 <= kj < maxj and 0 <= ki < maxi:
                if kj == j and ki == i:
                    continue
                else:
                    yield (ki, kj)


def increase_neighbours(i, j, data, to_flash, flashed):
    for ki, kj in neighbours(i, j, data):
        data[kj][ki] += 1
        if data[kj][ki] > 9 and (ki, kj) not in flashed:
            to_flash.add((ki, kj))


step = 0
flashed = set()
while len(flashed) < len(data) * len(data[0]):
    for j, line in enumerate(data):
        for i in range(len(line)):
            data[j][i] += 1

    to_flash = set()
    flashed = set()
    for j, line in enumerate(data):
        for i in range(len(line)):
            if data[j][i] > 9:
                to_flash.add((i, j))

    while to_flash:
        ki, kj = to_flash.pop()
        increase_neighbours(ki, kj, data, to_flash, flashed)
        flashed.add((ki, kj))

    for j, line in enumerate(data):
        for i in range(len(line)):
            if (i, j) in flashed:
                data[j][i] = 0

    step += 1

print("step:", step)
