def calc_checksum(blocks):

    checksum = 0
    for i, block in enumerate(blocks):
        checksum += i * int(block)

    return checksum


def move_blocks(blocks):

    i = 0
    last_i = len(blocks) - 1
    while i < last_i:

        if blocks[last_i] == ".":
            blocks.pop()
            last_i -= 1
        elif blocks[i] == ".":
            blocks[i] = blocks.pop()
            last_i -= 1
            i += 1
        else:
            i += 1

    while blocks:
        if blocks[-1] == ".":
            blocks.pop()
        else:
            break

    return blocks


def expand_disk_map(disk_map):

    expanded_map = []
    is_file = True
    id = 0
    while disk_map:
        block_item = disk_map.pop(0)
        if is_file:
            expanded_map.extend([id] * block_item)
            is_file = False
            id += 1
        else:
            expanded_map.extend(["."] * block_item)
            is_file = True

    return expanded_map


def main():

    # with open(".\day-09\input-sample.txt", "r") as file:
    with open(".\day-09\input.txt", "r") as file:
        input = file.readline()

    disk_map = list(map(int, list(input)))
    expanded_map = expand_disk_map(disk_map)
    sorted_blocks = move_blocks(expanded_map)
    total = calc_checksum(sorted_blocks)

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
