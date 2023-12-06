def get_ways(time, distance):
    return sum([1 if j * (time - j) > distance else 0 for j in range(0, time + 1)])


def solve2():
    return get_ways(58996469, 478223210191071)


def solve1(data):
    answer = 0
    rows = data.split("\n")
    time = [int(t) for t in rows[0].split(":")[1:][0].strip().split(" ") if t]
    dist = [int(t) for t in rows[1].split(":")[1:][0].strip().split(" ") if t]

    for i in range(0, len(time)):
        t = time[i]
        d = dist[i]
        answer = (answer or 1) * get_ways(t, d)

    return answer


if __name__ == "__main__":
    with open("input", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2())
