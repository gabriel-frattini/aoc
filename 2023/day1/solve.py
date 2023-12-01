WORD_NUMBERS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def find_num(i, j) -> int | None:
    return next((val for (num, val) in WORD_NUMBERS.items() if i[j:].find(num) == 0), None)


def solve(data):
    sum_ = 0
    for i in data.split("\n"):
        first = None
        last = None
        for j in range(0, len(i)):
            try:
                num = int(i[j])
            except ValueError:
                num = find_num(i, j)

            if num is None:
                continue

            if first is None:
                first = num

            last = num

        if first is None or last is None:
            continue

        sum_ += int(f"{first}{last}")

    return sum_


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve(data))
