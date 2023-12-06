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
    rows = data.split("\n\n")

    seeds = [int(seed) for seed in rows[0].split(": ")[1].split(" ") if seed]

    m_ = {}

    for row in rows[1:]:
        [from_, _, to_] = row.split("\n")[0].split(" ")[0].split("-")
        maps_ = filter(lambda m: m, row.split("\n")[1:])

        map_ = []
        for m in maps_:
            [dst, src, diff] = m.split(" ")
            map_.append({"dst": int(dst), "src": int(src), "max": int(src) + int(diff)})

        m_[from_] = {"from": from_, "to": to_, "map": map_}

    m_["location"] = {"from": "location", "to": None, "map": []}

    lowest = float("inf")
    for i in range(0, len(seeds) - 1, 2):
        seed_min, seed_range = seeds[i], seeds[i + 1]

        loc = walk_to_lowest_loc("seed", seed_min, seed_min + seed_range, m_)
        if loc < lowest:
            lowest = loc

    return lowest


def walk_to_lowest_loc(key, seed_min, seed_max, m):
    if m[key]["to"] is None:
        return seed_min

    for map_ in m[key]["map"]:

        if map_["src"] <= seed_min < map_["max"]:
            if seed_max < map_["max"]:
                new_min_seed = seed_min - map_["src"] + map_["dst"]
                new_max_seed = seed_max - map_["src"] + map_["dst"]
                return walk_to_lowest_loc(m[key]["to"], new_min_seed, new_max_seed, m)

            else:
                return min(
                    walk_to_lowest_loc(key, seed_min, map_["max"] - 1, m),
                    walk_to_lowest_loc(key, map_["max"], seed_max, m),
                )

    return walk_to_lowest_loc(m[key]["to"], seed_min, seed_max, m)


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
