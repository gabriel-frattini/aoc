def solve(data):

    max_calories = 0
    for elf in data.split("\n\n"):

        calories_sum = 0
        for cal in elf.split("\n"):

            calories_sum += int(cal) if cal else 0

        if calories_sum > max_calories:
            max_calories = calories_sum

    return max_calories


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve(data))
