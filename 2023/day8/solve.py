def map_paths(paths):
    m = {}
    for path in paths.split("\n"):
        if not path:
            continue
        [from_, dst] = path.split(" = ")

        [left, right] = dst[1:-1].split(",")
        m[from_] = {"L": left.strip(), "R": right.strip()}

    return m


def solve1(data):
    [seq, paths] = data.split("\n\n")
    m = map_paths(paths)
    node = "AAA"
    steps = 0

    def walk(node, seq, m, steps):
        if node == "ZZZ":
            return node, steps
        return (m[node][seq[steps % len(seq)]], steps + 1)

    while node != "ZZZ":
        node, steps = walk(node, seq, m, steps)

    return steps


def solve2(data):
    [seq, paths] = data.split("\n\n")
    m = map_paths(paths)
    nodes = [n for n in m.keys() if n[-1] == "A"]
    steps = 0

    while not all([n[-1] == "Z" for n in nodes]):
        for i in range(0, len(nodes)):
            nodes[i] = m[nodes[i]][seq[steps % len(seq)]]
        steps += 1

    return steps


if __name__ == "__main__":
    with open("input", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2(data))
