#!/usr/bin/env python3

# ['R 4', 'U 4', 'L 3', 'D 1', 'R 4', 'D 1', 'L 5', 'R 2']

visited = [(0, 0)]
with open("input.txt") as f:
    data = f.read().splitlines()


def get_points(wire):
    x = 0
    y = 0
    points = []
    points.append((x, y))

    last_move = None

    for move in wire:
        direction, distance = move[0], int(move[1:])

        if direction == "R":
            for i in range(distance):

                if i == 0:
                    if last_move == "U":
                        continue

                    elif last_move == "D":
                        continue

                if i == 1:
                    if last_move == "U":
                        x += 1
                        y += 1

                        if (x, y) not in points:
                            points.append((x, y))

                    elif last_move == "D":
                        x += 1
                        y -= 1
                        if (x, y) not in points:
                            points.append((x, y))

                else:
                    x += 1
                    if (x, y) not in points:
                        points.append((x, y))

        if direction == "L":
            for i in range(distance):

                if i == 0:
                    if last_move == "U":
                        continue
                    elif last_move == "D":
                        continue

                if i == 1:
                    if last_move == "U":
                        x -= 1
                        y += 1

                        if (x, y) not in points:
                            points.append((x, y))

                    elif last_move == "D":
                        x -= 1
                        y -= 1
                        if (x, y) not in points:
                            points.append((x, y))

                else:
                    x += 1
                    if (x, y) not in points:
                        points.append((x, y))

        if direction == "U":
            for i in range(distance):
                if i == 0:

                    if last_move == "R":
                        continue
                    elif last_move == "L":
                        continue

                if i == 1:
                    if last_move == "R":
                        x += 1
                        y += 1

                        if (x, y) not in points:
                            points.append((x, y))

                    elif last_move == "L":
                        x -= 1
                        y += 1
                        if (x, y) not in points:
                            points.append((x, y))

                else:
                    x += 1
                    if (x, y) not in points:
                        points.append((x, y))

        if direction == "D":
            for i in range(distance):
                if i == 0:
                    if last_move == "R":
                        continue
                    elif last_move == "L":
                        continue

                if i == 1:
                    if last_move == "R":
                        x += 1
                        y -= 1

                        if (x, y) not in points:
                            points.append((x, y))

                    elif last_move == "L":
                        x -= 1
                        y -= 1
                        if (x, y) not in points:
                            points.append((x, y))

                else:
                    x += 1
                    if (x, y) not in points:
                        points.append((x, y))

        last_move = direction
    return points


print(get_points(data))
print(len(get_points(data)))
