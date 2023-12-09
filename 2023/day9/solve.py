def walk(nums):

    if not all(i == 0 for i in nums) == 0:
        return 0
    m = []
    for i in range(len(nums) - 1):
        m.append(nums[i + 1] - nums[i])

    return nums[-1] + walk(m)


def solve1(data):
    rows = [[int(num) for num in nums.split(" ")] for nums in data.split("\n") if nums]
    return sum(walk(nums) for nums in rows)


def solve2(data):
    rows = [[int(num) for num in nums.split(" ")] for nums in data.split("\n") if nums]
    return sum(walk([n for n in reversed(nums)]) for nums in rows)


if __name__ == "__main__":
    with open("input", "r") as f:
        data = f.read()

    print(solve1(data))
    print(solve2(data))
