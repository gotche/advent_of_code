import sys
from collections import defaultdict, Counter
from dataclasses import dataclass

# read file
data = sys.stdin.readlines()

# clean
d = []

for line in data:
    signal, display = line.split("|")
    d.append((signal.split(), display.split()))

# preparation
digits = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}


lengths = [None, None, 1, 7, 4, set([2, 3, 5]), set([0, 6, 9]), 8]

numbers = 0
for line in d:
    for display in line[1]:
        if len(display) in [2, 3, 4, 7]:
            numbers += 1

print(numbers)
