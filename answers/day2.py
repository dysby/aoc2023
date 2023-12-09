import re
from io import TextIOBase
from typing import List
import math
import operator
import functools


def is_valid(game_list: List[dict], baseline: dict):
    for game in game_list:
        for color, value in game.items():
            # print(value, baseline[color])
            if value > baseline[color]:
                return False
    return True


def power_set_cubes(game_list: List[dict]):
    # for game in game_list:
    #     for color, value in game:
    #         min_colors[color] = min(value, min_colors[color])
    min_colors = {"red": 0, "green": 0, "blue": 0}
    for game in game_list:
        for color, value in game.items():
            # min_colors.setdefault(color, []).append(value)
            min_colors[color] = max(min_colors[color], value)

    # min_colors = {color: max(values) for color, values in min_colors.items()}

    game_power = functools.reduce(operator.mul, min_colors.values())
    return game_power


def answer(input_file: TextIOBase):
    data = input_file.read().splitlines()

    baseline = {"red": 12, "green": 13, "blue": 14}

    games = {}
    for line in data:
        game_id = int(line[5 : line.index(":")])
        for game_config_line in line[line.index(":") + 1 :].split(";"):
            sub_game = {}
            for color_config in game_config_line.split(","):
                m = re.search(r"(\d+) (\w+)", color_config)
                number, color = int(m.group(1)), m.group(2)
                sub_game[color] = number

            games.setdefault(game_id, []).append(sub_game)

    part1 = sum(
        [
            game_id
            for game_id, game_list in games.items()
            if is_valid(game_list, baseline)
        ]
    )
    print(f"Day 1, part1 answer = {part1}")

    part2 = sum([power_set_cubes(game_list) for _, game_list in games.items()])
    print(f"Day 1, part2 answer = {part2}")
