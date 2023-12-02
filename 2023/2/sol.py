from collections import namedtuple
from parse import parse
from math import prod


input_file = "input2"
colors = ("blue", "green", "red")  # alphabetically ordered
Game = namedtuple("Game", colors)


def load_input(input_file):
    with open(input_file) as file:
        games = [line.strip() for line in file.readlines()]

    return games


def parse_line(line):
    game_id, rest = line.split(":")

    game_id = parse("Game {}", game_id)[0]
    games = rest.split(";")
    games_tupes = []

    for game in games:
        color_list = [0, 0, 0]
        for selection in game.split(","):
            for id, color in enumerate(colors):
                if match := parse(f"{{}} {color}", selection):
                    color_list[id] = int(match[0])

        games_tupes.append(Game(*color_list))

    return game_id, games_tupes


def test_parse_line():
    line = "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"
    output = ("1", [Game(3, 0, 4), Game(6, 2, 1), Game(0, 2, 0)])
    assert parse_line(line) == output, parse_line(line)

    line = (
        "Game 100: 5 green, 7 red, 4 blue; 11 green, 9 red, 8 blue; 2 blue, 12 green\n"
    )
    output = ("100", [Game(4, 5, 7), Game(8, 11, 9), Game(2, 12, 0)])
    assert parse_line(line) == output, parse_line(line)


def load_games(input_file):
    return dict([parse_line(line) for line in load_input(input_file)])


biggest_game = Game(blue=14, green=13, red=12)
games = load_games(input_file)

impossible = []

for game_id, selections in games.items():
    for selection in selections:
        if (
            selection.blue > biggest_game.blue
            or selection.green > biggest_game.green
            or selection.red > biggest_game.red
        ):
            impossible.append(game_id)

subset = games.keys() - set(impossible)
print(sum(int(i) for i in subset))

# part 2
powers = []
for game_id, selections in games.items():
    counter = [0, 0, 0]
    for selection in selections:
        for i, color in enumerate(selection):
            if counter[i] < color:
                counter[i] = color

    powers.append(prod(counter))

print(sum(powers))
