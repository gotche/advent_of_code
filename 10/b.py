import sys
from collections import deque

# read file
data = sys.stdin.readlines()

# clean
data = [list(line.strip()) for line in data]
pairs = {
    "(": ")",
    "[": "]",
    "<": ">",
    "{": "}",
}
scores = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
    None: 0,
}

# process


def process(line, pile):

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


def finish(pile):
    while pile:
        element = pile.pop()
        yield pairs[element]


final_score = []
for line in data:
    pile = []
    if process(line, pile) is None:
        result = 0
        for i in finish(pile):
            result *= 5
            result += scores[i]

        final_score.append(result)

print(sorted(final_score)[len(final_score) // 2])
