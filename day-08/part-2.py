import itertools


def number_of_antinodes(ant_1, ant_2, max_x, max_y):

    nodes = set()

    x1 = ant_1[0]
    y1 = ant_1[1]
    x2 = ant_2[0]
    y2 = ant_2[1]

    x_diff = x2 - x1
    y_diff = abs(y2 - y1)
    if y1 < y2:
        y_dir = 1
    else:
        y_dir = -1

    x = x1
    y = y1
    while True:
        # print(f"L:{x}, {y}, {y_dir}, [{max_x}|{max_y}]")
        nodes.add((x, y))
        x = x - x_diff
        y = y - y_diff * y_dir

        if x < 0 or (y_dir == 1 and y < 0) or (y_dir == -1 and y >= max_y):
            break

    x = x2
    y = y2
    while True:
        # print(f"H:{x}, {y}, {y_dir}, [{max_x}|{max_y}]")
        nodes.add((x, y))
        x = x + x_diff
        y = y + y_diff * y_dir

        if x >= max_x or (y_dir == 1 and y >= max_y) or (y_dir == -1 and y < 0):
            break

    # print(nodes)
    return nodes


def valid_char(char):
    return char.isupper() or char.islower() or char.isdigit()


def main():

    # with open(".\day-08\input-sample.txt", "r") as file:
    with open(".\day-08\input.txt", "r") as file:
        input = file.read()

    grid = [list(row) for row in input.splitlines()]

    total_rows = len(grid)
    total_cols = len(grid[0])

    antennas = {}
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if not valid_char(grid[row][col]):
                continue

            if grid[row][col] in antennas:
                antennas[grid[row][col]].append((row, col))
            else:
                antennas[grid[row][col]] = [(row, col)]

    unique_nodes = set()
    for locations in antennas.values():
        combos = list(itertools.combinations(locations, 2))
        for combo in combos:
            nodes = number_of_antinodes(combo[0], combo[1], total_rows, total_cols)
            for node in nodes:
                unique_nodes.add(node)

    total = len(unique_nodes)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
