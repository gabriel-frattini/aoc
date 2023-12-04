def gen_games(data):
    rows = data.split("\n")
    for i in range(0, len(rows)):
        row = rows[i]

        if not row:
            continue

        [left_col, right_col] = row.split("|")

        [card, nums] = left_col.split(":")
        id_ = int(card.split("Card")[-1].strip())

        winnings = [num for num in nums.split(" ") if num not in ["", " "]]
        cards = [num for num in right_col.split(" ") if num not in ["", " "]]

        yield (id_, winnings, cards)


def solve1(data):
    sum_ = 0
    for game in gen_games(data):
        if game is None:
            continue
        _, winnings, cards = game

        cnt = len([win for win in winnings if win in cards])
        if cnt > 0:
            sum_ += 2 ** (cnt - 1)

    return sum_


def solve2(data):
    instances = {}
    for game in gen_games(data):
        if game is None:
            continue
        id_, winnings, cards = game

        if id_ in instances:
            instances[id_] += 1
        else:
            instances[id_] = 1

        cnt = len([win for win in winnings if win in cards]) + 1

        for k in range(id_ + 1, id_ + cnt):
            if k not in instances:
                instances[k] = 0

            instances[k] += instances[id_]

    return sum(cnt for cnt in instances.values())


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2(data))
