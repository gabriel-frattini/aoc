from collections import deque
from functools import reduce


with open("input.txt") as f:
    data = f.read()

monkeys = []

for i in data.split("\n\n"):
    lines = i.splitlines()

    items = deque([int(i) for i in lines[1].split(": ")[1].split(", ")])

    op = lines[2].split("= ")[1]
    op = eval(f"lambda old: {op}")

    test_div = int(lines[3].split(" ")[-1])
    if_true = int(lines[4].split(" ")[-1])
    if_false = int(lines[5].split(" ")[-1])

    monkeys.append(
        {
            "items": items,
            "op": op,
            "test_div": test_div,
            "if_true": if_true,
            "if_false": if_false,
            "inspected": 0,
        }
    )

rounds = 0
stuff_slinging_simian_shenanigans = True

while stuff_slinging_simian_shenanigans:
    rounds += 1
    for monkey in monkeys:
        while len(monkey["items"]) > 0:
            item = monkey["items"].pop()

            item = monkey["op"](item)
            item = item // 3

            next_monkey = (
                monkey["if_true"]
                if item % monkey["test_div"] == 0
                else monkey["if_false"]
            )
            monkeys[next_monkey]["items"].append(item)

            monkey["inspected"] += 1

    if rounds == 20:
        stuff_slinging_simian_shenanigans = False

print(
    reduce(
        (lambda x, y: x * y),
        sorted([monkey["inspected"] for monkey in monkeys], reverse=True)[:2],
    )
)
