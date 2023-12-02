from typing import Generator


BAG_CONFIG = {"red": 12, "green": 13, "blue": 14}


def game_to_subgames(game: str) -> Generator[dict[str, int], None, None]:
    groups: list[str] = game.split(":")[1].split(";")
    for set_ in groups:
        subsets = set_.split(",")

        subgame = {}
        for cube in subsets:
            if not cube:
                continue
            count, color = cube.split(" ")[1:]
            subgame[color] = int(count)

        yield subgame


def get_valid_games(data):
    for game in data.split("\n"):
        bad = False
        if not game:
            continue
        for subgame in game_to_subgames(game):
            if broke_limit(subgame):
                bad = True

        if not bad:
            yield game


def get_most_cubes(data):
    for game in data.split("\n"):
        if not game:
            continue

        most = {}
        for subgame in game_to_subgames(game):

            for color, count in subgame.items():
                if color not in most or count > most[color]:
                    most[color] = count

        yield most


def broke_limit(config):
    return any(color for color, count in config.items() if BAG_CONFIG[color] < int(count))


def solve1(data):
    sum_ = 0
    for game in get_valid_games(data):
        id_ = int(game[5:].split(":")[0])
        sum_ += id_

    return sum_


def solve2(data):
    sum_ = 0
    for most in get_most_cubes(data):
        power = 1
        for count in most.values():
            power *= count
        sum_ += power
    return sum_


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2(data))
