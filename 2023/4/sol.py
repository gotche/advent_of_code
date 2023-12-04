input_file = "input2"


def load_input(input_file):
    with open(input_file) as file:
        lines = [line.strip() for line in file.readlines()]

    return lines


def parse_cards(lines):
    cards = []
    for line in lines:
        numbers = line.split(":")[1]
        left, right = numbers.split("|")
        win = [int(i) for i in left.split()]
        choices = [int(i) for i in right.split()]
        cards.append((win, choices))

    return cards


lines = load_input(input_file)
cards = parse_cards(lines)

total = 0

for card in cards:
    matches = len(set(card[0]).intersection(set(card[1])))
    if matches > 0:
        total += 2 ** (matches - 1)

print(total)
