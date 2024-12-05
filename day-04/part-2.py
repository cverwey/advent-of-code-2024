def boundary_test(grid, row, col, row_offset, col_offset, word_len):

    if col_offset == 1:
        if col > len(grid[row]) - word_len:
            return False

    if col_offset == -1:
        if col < word_len - 1:
            return False

    if row_offset == 1:
        if row > len(grid) - word_len:
            return False

    if row_offset == -1:
        if row < word_len - 1:
            return False

    return True


def is_word(grid, row, col, row_offset, col_offset, word):

    if word == "":
        return True

    if grid[row][col] != word[0]:
        return False

    return is_word(
        grid, row + row_offset, col + col_offset, row_offset, col_offset, word[1:]
    )


def word_search(grid, row, col, row_offset, col_offset, word):

    if not boundary_test(grid, row, col, row_offset, col_offset, len(word)):
        return False

    return is_word(grid, row, col, row_offset, col_offset, word)


def grid_search(grid, word):

    total = 0
    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if word_search(grid, row, col, -1, 1, word):
                # print(f"[{row}, {col}] north-east")
                total = total + 1

            if word_search(grid, row, col, 1, 1, word):
                # print(f"[{row}, {col}] south-east")
                total = total + 1

            if word_search(grid, row, col, 1, -1, word):
                # print(f"[{row}, {col}] south-west")
                total = total + 1

            if word_search(grid, row, col, -1, -1, word):
                # print(f"[{row}, {col}] north-west")
                total = total + 1

    if total == 2:
        return 1

    return 0


def get_sub_grid(grid, row_start, col_start, grid_len):
    return [
        row[col_start : col_start + grid_len]
        for row in grid[row_start : row_start + grid_len]
    ]


def main():

    # with open(".\day-04\input-sample.txt", "r") as file:
    with open(".\day-04\input.txt", "r") as file:
        input = file.read()

    word = "MAS"
    grid = [list(row) for row in input.splitlines()]

    total = 0
    for row in range(len(grid) - len(word) + 1):
        for col in range(len(grid[row]) - len(word) + 1):
            subgrid = get_sub_grid(grid, row, col, len(word))
            total = total + grid_search(subgrid, word)

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
