def is_increasing(record):
    for i in range(1, len(record)):
        if record[i] <= record[i - 1]:
            return False
    return True


def is_decreasing(record):
    for i in range(1, len(record)):
        if record[i] >= record[i - 1]:
            return False
    return True


def is_in_range(record):
    for i in range(1, len(record)):
        difference = abs(record[i] - record[i - 1])
        if difference > 3 or difference < 1:
            return False
    return True


def main():
    with open(r".\day-02\input.txt", "r") as file:
        content = file.read()

    safe_count = 0
    for line in content.splitlines():
        report = list(map(int, line.split()))
        safe = (is_increasing(report) or is_decreasing(report)) and is_in_range(report)
        if safe:
            safe_count = safe_count + 1

    print(safe_count)


if __name__ == "__main__":
    main()
