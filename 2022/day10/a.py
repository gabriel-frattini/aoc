#!/usr/bin/env python3

import subprocess

data = (
    subprocess.run(
        "cat input.txt \
    | sed 's/ /,/' \
    | sed 's/noop/1,0/' \
    | sed 's/addx/2/' | xargs",
        shell=True,
        capture_output=True,
    )
    .stdout.decode("utf-8")
    .split(" ")
)

res = 1
total_cycles = 0
answer = 0
for op in data:
    cycles, value = int(op.split(",")[0]), int(op.split(",")[1])

    for _ in range(cycles):
        total_cycles += 1

        if total_cycles == 20:
            answer += 20 * res
        if total_cycles == 60:
            answer += 60 * res
        if total_cycles == 100:
            answer += 100 * res
        if total_cycles == 140:
            answer += 140 * res
        if total_cycles == 180:
            answer += 180 * res
        if total_cycles == 220:
            answer += 220 * res

    res += value


print(answer)
