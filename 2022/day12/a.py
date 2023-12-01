#!/usr/bin/env python3
from typing import List


with open("input.txt") as f:
    data = f.read().splitlines()


def get_neighbours(x, y, data) -> List[str]:
    neighbours = []
    for i in range(-1, 2):
        for j in range(-1, 2):
            if i == 0 and j == 0:
                continue
            if 0 <= x + i < len(data):
                neighbours.append(data[x + i][y])
            if 0 <= y + j < len(data[0]):
                neighbours.append(data[x][y + j])
    return [n for n in neighbours if n != "S"]


path = [data[0][0]]
for i in range(len(data)):
    for j in range(len(data[i])):
        me = data[i][j]
        neighbours = get_neighbours(i, j, data)
        if me == "S":
            path.append(sorted(neighbours)[0])
            break
        else:
            for neighbour in neighbours:
                if ord(neighbour) == ord(me) or ord(neighbour) == ord(me) + 1:
                    path.append(neighbour)
                    break


print("".join(path))
