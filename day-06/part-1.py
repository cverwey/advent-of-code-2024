def find_guard(grid):
    for row in range(len(grid)):
        if "^" in grid[row]:
            return (row, grid[row].index("^"))


def turn_90(direction):
    if direction == (-1, 0):
        return (0, 1)
    if direction == (0, 1):
        return (1, 0)
    if direction == (1, 0):
        return (0, -1)
    if direction == (0, -1):
        return (-1, 0)


def walk_positions(grid, pos, direction):

    positions = set()
    while True:

        # identify next position
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        # reach top or bottom border
        if next_pos[0] == -1 or next_pos[0] == len(grid):
            positions.add(pos)
            break

        # reach left or right border
        if next_pos[1] == -1 or next_pos[1] == len(grid[pos[0]]):
            positions.add(pos)
            break

        # move to next position
        if grid[next_pos[0]][next_pos[1]] == ".":
            positions.add(pos)
            pos = next_pos

        # turn 90 degrees
        else:
            direction = turn_90(direction)

    return positions


def main():

    # with open(".\day-06\input-sample.txt", "r") as file:
    with open(".\day-06\input.txt", "r") as file:
        input = file.read()

    grid = [list(row) for row in input.splitlines()]
    pos = find_guard(grid)
    grid[pos[0]][pos[1]] = "."
    direction = (-1, 0)

    positions = walk_positions(grid, pos, direction)
    total = len(positions)
    print(f"Total: {total}")


if __name__ == "__main__":
    main()
