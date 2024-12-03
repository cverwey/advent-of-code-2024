import re


def main():

    # with open(".\day-03\input-sample.txt", "r") as file:
    with open(".\day-03\input.txt", "r") as file:
        input = file.read()

    regex = r"mul\((\d{1,3}),(\d{1,3})\)"
    matches = re.findall(regex, input)

    total = 0
    for match in matches:
        total = total + int(match[0]) * int(match[1])
    print(total)


if __name__ == "__main__":
    main()
