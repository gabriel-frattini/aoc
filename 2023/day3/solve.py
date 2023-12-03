SYMBOLS = ["-", "*", "&", "$", "@", "#", "=", "/", "+", "%"]

DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]


def parse_num(i, j, rows):
    cell = rows[i][j]
    if not cell.isdigit():
        return None

    num = ""

    k = j
    while rows[i][k - 1].isdigit():
        k -= 1

    while k < len(rows[i]) and rows[i][k].isdigit():
        num = f"{num}{rows[i][k]}"
        k += 1

    return int(num) or None


def get_neighbors_to_symbol(i, j, rows, symbols):
    neighbors = []

    k = -1
    l = -1

    while k < 2:
        l = -1
        while l < 2:
            try:
                if rows[i + k][j + l] in symbols:
                    neighbor = parse_num(i + k, j + l, rows)
                    if neighbor:
                        neighbors.append(neighbor)
                        l += len(str(neighbor))

            except BaseException as e:
                # index out of bounce
                pass

            l += 1
        k += 1

    return neighbors


def solve1(data):
    sum_ = 0
    rows = data.split("\n")
    for i in range(0, len(rows)):
        row = rows[i]

        j = 0
        while j < len(row):
            num = parse_num(i, j, rows)

            if not num:
                j += 1
                continue

            for k in range(j, j + len(str(num)) + 1):
                neighbors = get_neighbors_to_symbol(i, k, rows, SYMBOLS)
                if len(neighbors) > 0:
                    sum_ += int(num)
                    break

            j += len(str(num))
            continue
        j += 1

    return sum_


def solve2(data):
    sum_ = 0
    rows = data.split("\n")
    for i in range(0, len(rows)):
        row = rows[i]

        j = 0
        while j < len(row):
            cell = row[j]

            if not cell:
                continue

            if cell == "*":
                neighbors = get_neighbors_to_symbol(i, j, rows, DIGITS)
                if len(neighbors) == 2:
                    [fst, snd] = neighbors
                    sum_ += fst * snd

            j += 1

    return sum_


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2(data))
