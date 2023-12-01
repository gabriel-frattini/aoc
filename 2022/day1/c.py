def solve(data):

    return [
        sum([int(cal) for cal in elf.split("\n") if cal]) for elf in data.split("\n\n")
    ].sort(reverse=True)[:3]


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        print(solve(f.read()))
