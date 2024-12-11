def calc_checksum(blocks):

    checksum = 0
    index = 0
    for block in blocks:
        for j in range(block[1]):
            if block[0] != ".":
                checksum += (index + j) * int(block[0])
        index += j + 1

    return checksum


def move_blocks(blocks):

    searched_indices = []

    for last_i in range(len(blocks) - 1, -1, -1):

        # print(f"last_i: {last_i} | {blocks[last_i]}")
        if blocks[last_i][0] == ".":
            continue

        i = 0
        while i < last_i:
            if blocks[i][0] == ".":
                last_size = blocks[last_i][1]
                i_size = blocks[i][1]
                if i_size >= last_size:
                    index = blocks[last_i][0]
                    if index not in searched_indices:
                        diff = i_size - last_size
                        blocks[i] = blocks[last_i]
                        blocks[last_i] = (".", last_size)
                        if diff > 0:
                            # if next block contains empties, add to it
                            if blocks[i + 1][0] == ".":
                                blocks[i + 1][1] += diff
                            # else insert new block
                            else:
                                blocks.insert(i + 1, (".", diff))
                            last_i += 1

                        searched_indices.append(index)
                        break

            i += 1

    return blocks


def expand_disk_map(disk_map):

    expanded_map = []
    is_file = True
    id = 0
    while disk_map:
        block_item = disk_map.pop(0)
        if is_file:
            expanded_map.append((id, block_item))
            is_file = False
            id += 1
        else:
            if block_item != 0:
                expanded_map.append((".", block_item))
            is_file = True

    return expanded_map


def convert_pairs_to_string(blocks):
    block_str = ""
    for block in blocks:
        block_str += str(block[0]) * block[1]

    return block_str


def main():

    # with open(".\day-09\input-sample.txt", "r") as file:
    with open(".\day-09\input.txt", "r") as file:
        input = file.readline()

    disk_map = list(map(int, list(input)))
    # print(disk_map)
    expanded_map = expand_disk_map(disk_map)
    # print(expanded_map)
    sorted_blocks = move_blocks(expanded_map)
    # print(sorted_blocks)
    total = calc_checksum(sorted_blocks)

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
