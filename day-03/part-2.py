import re


def main():

    # with open(".\day-03\input-sample-2.txt", "r") as file:
    with open(".\day-03\input.txt", "r") as file:
        input = file.read()

    regex = r"(mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don't\(\))"
    matches = re.findall(regex, input)

    do = True
    total = 0
    for match in matches:
        if match[0] == "do()":
            do = True
        elif match[0] == "don't()":
            do = False
        elif do:
            total = total + int(match[1]) * int(match[2])

    print(total)


if __name__ == "__main__":
    main()
