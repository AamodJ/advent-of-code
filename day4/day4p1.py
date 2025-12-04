import numpy as np

with open("input.txt", "r") as fd:
    s = fd.readlines()


def count_neighbours(locs: np.ndarray, x: int, y: int) -> int:
    neighbour_count = 0
    for offsetY in [-1, 0, 1]:
        for offsetX in [-1, 0, 1]:
            if (
                y + offsetY not in range(locs.shape[0])
                or x + offsetX not in range(locs.shape[1])
                or (offsetX == 0 and offsetY == 0)
            ):
                continue
            elif locs[x + offsetX, y + offsetY] == "@":
                neighbour_count += 1
                if x == 2 and y == 0:
                    print(
                        f"Found neighbour at {x + offsetX}, {y + offsetY} for {x}, {y}"
                    )

    return neighbour_count


locs = np.array([[col for col in row] for row in s])[:, :-1]
accessible_rolls = 0
for y in range(locs.shape[0]):
    for x in range(locs.shape[1]):
        if locs[x, y] == "@" and count_neighbours(locs, x, y) < 4:
            accessible_rolls += 1

print(f"Number of accessible paper rolls: {accessible_rolls}")
