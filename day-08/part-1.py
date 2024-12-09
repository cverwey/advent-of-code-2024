import itertools


def number_of_antinodes(ant_1, ant_2, max_x, max_y):

    nodes = []

    x1 = ant_1[0]
    y1 = ant_1[1]
    x2 = ant_2[0]
    y2 = ant_2[1]

    x_diff = x2 - x1
    y_diff = abs(y2 - y1)

    x3 = x1 - x_diff
    x4 = x2 + x_diff

    if y1 < y2:
        y3 = y1 - y_diff
        y4 = y2 + y_diff
    else:
        y3 = y1 + y_diff
        y4 = y2 - y_diff

    if x3 < 0 or x3 >= max_x or y3 < 0 or y3 >= max_y:
        pass
    else:
        nodes.append((x3, y3))

    if x4 < 0 or x4 >= max_x or y4 < 0 or y4 >= max_y:
        pass
    else:
        nodes.append((x4, y4))

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
