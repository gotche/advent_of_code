import sys
from collections import deque

# read file
data = sys.stdin.readlines()

# clean
data = [list(line.strip()) for line in data]

# problem mappings
pairs = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}
scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    None: 0,
}

# process


def process(line):
    pile = []

    for element in line:
        if element in pairs:
            pile.append(element)
            continue

        if len(pile) == 0:
            return element

        if not is_pair(pile.pop(), element):
            return element


def is_pair(a, b):
    return pairs[a] == b


print(sum(scores[process(line)] for line in data))
