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

total_cards = 1

total_matches = []
for card in cards:
    matches = len(set(card[0]).intersection(set(card[1])))
    total_matches.append(matches)

acum = [1] * len(total_matches)
for i, match in enumerate(total_matches):
    for j in range(match):
        acum[i + j + 1] += acum[i]

print(sum(acum))
