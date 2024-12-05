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


def main():

    # with open(".\day-04\input-sample.txt", "r") as file:
    with open(".\day-04\input.txt", "r") as file:
        input = file.read()

    word = "XMAS"
    grid = [list(row) for row in input.splitlines()]
    total = 0

    for row in range(len(grid)):
        for col in range(len(grid[row])):

            if word_search(grid, row, col, -1, 0, word):
                # print(f"[{row}, {col}] north")
                total = total + 1

            if word_search(grid, row, col, -1, 1, word):
                # print(f"[{row}, {col}] north-east")
                total = total + 1

            if word_search(grid, row, col, 0, 1, word):
                # print(f"[{row}, {col}] east")
                total = total + 1

            if word_search(grid, row, col, 1, 1, word):
                # print(f"[{row}, {col}] south-east")
                total = total + 1

            if word_search(grid, row, col, 1, 0, word):
                # print(f"[{row}, {col}] south")
                total = total + 1

            if word_search(grid, row, col, 1, -1, word):
                # print(f"[{row}, {col}] south-west")
                total = total + 1

            if word_search(grid, row, col, 0, -1, word):
                # print(f"[{row}, {col}] west")
                total = total + 1

            if word_search(grid, row, col, -1, -1, word):
                # print(f"[{row}, {col}] north-west")
                total = total + 1

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
