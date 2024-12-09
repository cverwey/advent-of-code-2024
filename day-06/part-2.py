import copy
import time


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

    positions = []
    positions_and_direction = set()

    while True:

        # identify guard stuck in loop
        if (pos, direction) in positions_and_direction:
            return []

        # identify next position
        next_pos = (pos[0] + direction[0], pos[1] + direction[1])

        # reach top or bottom border
        if next_pos[0] == -1 or next_pos[0] == len(grid):
            if pos not in positions:
                positions.append(pos)
            positions_and_direction.add((pos, direction))
            break

        # reach left or right border
        if next_pos[1] == -1 or next_pos[1] == len(grid[pos[0]]):
            if pos not in positions:
                positions.append(pos)
            positions_and_direction.add((pos, direction))
            break

        # move to next position
        if grid[next_pos[0]][next_pos[1]] == ".":
            if pos not in positions:
                positions.append(pos)
            positions_and_direction.add((pos, direction))
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
    obstacles = 0

    print(positions[0])
    print(len(positions))

    for visited_pos in positions[1:]:
        row = visited_pos[0]
        col = visited_pos[1]

        obstacle_grid = copy.deepcopy(grid)
        if obstacle_grid[row][col] == ".":
            obstacle_grid[row][col] = "O"

        visited_positions = walk_positions(obstacle_grid, pos, direction)

        if not visited_positions:
            obstacles = obstacles + 1

    print(f"Total: {obstacles}")
    # 1480


if __name__ == "__main__":
    start_time = time.time()

    main()

    execution_time = time.time() - start_time

    # Convert to minutes, seconds, and milliseconds
    minutes = int(execution_time // 60)
    seconds = int(execution_time % 60)
    milliseconds = int((execution_time * 1000) % 1000)

    # Print the result
    print(
        f"Execution time: {minutes} minutes, {seconds} seconds, {milliseconds} milliseconds"
    )
