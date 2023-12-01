#!/usr/bin/env python3
with open("input.tmp", "r") as f:
    data = f.read().split(",")


pwd = "/"
fs = {pwd: 0}
sums = 0
for cmd in data:

    if cmd.isdigit():
        fs[pwd] += int(cmd)

    if cmd.startswith("cd"):

        to = cmd.split(" ")[1]

        if to == "..":
            pwd = pwd.rsplit("/", 1)[0] + "/"
        else:
            pwd = pwd + cmd.split(" ")[1] + "/"
            if pwd not in fs:
                fs[pwd] = 0

print(fs)
print(sum({v for v in fs.values() if v < 100_000}))
