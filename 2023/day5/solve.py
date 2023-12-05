def find_min_location(rows, paths):
    i = 2
    while i < len(rows):
        row = rows[i]

        if ":" not in row:
            i += 1
            continue

        for path in paths:
            last_num = path[-1]
            j = i
            while True:
                j += 1
                if not rows[j]:
                    break

                [dst, src, rng] = [int(num) for num in rows[j].split(" ")]

                if not src <= last_num <= src + rng - 1:
                    continue

                offset = last_num - src
                path.append(dst + offset)

        i += 1

    return min([path[-1] for path in paths])


def solve2(data):
    paths = []
    rows = data.split("\n")
    seeds = [int(seed) for seed in rows[0].split(": ")[1].split(" ")]

    for i in range(0, len(seeds) - 1, 2):
        for j in range(seeds[i], seeds[i] + seeds[i + 1]):
            paths.append([j])

    return find_min_location(rows, paths)


def solve1(data):
    paths = []
    rows = data.split("\n")
    seeds = [int(seed) for seed in rows[0].split(": ")[1].split(" ")]

    for seed in seeds:
        paths.append([seed])

    return find_min_location(rows, paths)


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2(data))
