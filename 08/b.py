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


def solve(lst) -> int:
    lengths = [None, None, 1, 7, 4, set([2, 3, 5]), set([0, 9, 6]), 8]
    numbers = [None] * 10

    # first add the candidates with length 5 and 6
    guess = {5: set(), 6: set()}

    sol = {}
    for display in lst[0] + lst[1]:
        l = len(display)
        if l in [5, 6]:
            guess[l].add("".join(sorted([i for i in display])))

        else:
            sol[display] = lengths[len(display)]
            numbers[lengths[len(display)]] = display

    # only the real number 6 will have 1 segment more than the number 1
    for i in guess[6]:
        if set(numbers[1]) - set(i):
            numbers[6] = i
            guess[6].remove(i)
            break

    # only the real number 4 will have more than 0 segments than the number 0
    for i in guess[6]:
        if set(numbers[4]) - set(i):
            numbers[0] = i
            guess[6].remove(i)
            break

    # 9 is the number left
    numbers[9] = guess[6].pop()

    # the segments of number 1 - the segments of number 3 are 0
    for i in guess[5]:
        if len(set(numbers[1]) - set(i)) == 0:
            numbers[3] = i
            guess[5].remove(i)
            break

    for i in guess[5]:
        if len(set(numbers[6]) - set(i)) == 1:
            numbers[5] = i
            guess[5].remove(i)
            break

    numbers[2] = guess[5].pop()

    mapping = {
        "".join(sorted(i for i in value)): index for index, value in enumerate(numbers)
    }

    sol = [str(mapping["".join(sorted(number))]) for number in lst[1]]
    final = int("".join(sol))

    return final


print(sum(solve(i) for i in d))
