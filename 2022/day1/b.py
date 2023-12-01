def solve(data):

    calories_list = []
    for elf in data.split("\n\n"):

        calories_sum = 0
        for cal in elf.split("\n"):

            calories_sum += int(cal) if cal else 0

        calories_list.append(calories_sum)

    sorted_calories_list = sorted(calories_list, reverse=True)

    return sum(sorted_calories_list[:3])


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        data = f.read()

    print(solve(data))
