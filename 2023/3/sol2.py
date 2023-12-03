from collections import namedtuple


input_file = "input2"
Point = namedtuple("Point", "i j")


def load_input(input_file):
    with open(input_file) as file:
        lines = [list(line.strip()) for line in file.readlines()]

    return lines


def find_simbol(lines):
    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            if char == "*":
                yield (i, j)


def find_numbers(lines):
    numbers = []
    number = []
    position = []

    for i, line in enumerate(lines):
        if number:
            numbers.append([int("".join(number)), [i - 1, position]])
            number = []
            position = []
        for j, char in enumerate(line):
            if char.isdecimal():
                number.append(char)
                position.append(j)
            else:
                if number:
                    numbers.append([int("".join(number)), [i, position]])
                    number = []
                    position = []

    if number:
        numbers.append([int("".join(number)), [i - 1, position]])
        number = []
        position = []

    return numbers


def numbers_to_dict(numbers):
    # [[467, [0, [0, 1, 2]]], [114, [0, [5, 6, 7]]], ...
    numbers_dict = {}
    for number in numbers:
        for position in number[1][1]:
            numbers_dict[(number[1][0], position)] = (
                number[0],
                (number[1][0], number[1][1][0]),
            )

    return numbers_dict


def find_adjacents(point, max_point):
    adj = []
    i, j = point.i, point.j

    if point.i > 0:
        adj.append(Point(i - 1, j))
        if point.j > 0:
            adj.append(Point(i - 1, j - 1))

        if point.j < max_point.j:
            adj.append(Point(i - 1, j + 1))
    if point.j > 0:
        adj.append(Point(i, j - 1))
    if point.i < max_point.i:
        adj.append(Point(i + 1, j))
        if point.j > 0:
            adj.append(Point(i + 1, j - 1))

        if point.j < max_point.j:
            adj.append(Point(i + 1, j + 1))

    if point.j < max_point.j:
        adj.append(Point(i, j + 1))

    return adj


the_map = load_input(input_file)
numbers = find_numbers(the_map)
max_point = Point(len(the_map), len(the_map[0]))

numbers_dict = numbers_to_dict(numbers)

total = 0

for symbol in find_simbol(the_map):
    num_per_symbol = set()
    adjs = find_adjacents(Point(*symbol), max_point)
    for adj in adjs:
        if (adj.i, adj.j) in numbers_dict:
            num_per_symbol.add(numbers_dict[(adj.i, adj.j)])

    if len(num_per_symbol) == 2:
        num1 = num_per_symbol.pop()
        num2 = num_per_symbol.pop()
        total += num1[0] * num2[0]

print(total)
