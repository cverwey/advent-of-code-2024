import itertools
import re


def eval_left_to_right(expression):

    tokens = re.findall(r"\d+|[-+*/]|\|\|", expression)

    # Initialize the result with the first number
    result = int(tokens[0])

    # Iterate over the operators and numbers
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        next_num = int(tokens[i + 1])

        # Perform the operation from left to right
        if operator == "+":
            result += next_num
        elif operator == "-":
            result -= next_num
        elif operator == "*":
            result *= next_num
        elif operator == "/":
            result /= next_num
        elif operator == "||":
            result = int(f"{result}{next_num}")

    return result


def find_valid_equation(answer, components):

    operations = ["+", "*", "||"]
    combinations = list(itertools.product(operations, repeat=len(components) - 1))

    for combination in combinations:
        zipped = itertools.zip_longest(components, combination, fillvalue="")
        flat = list(itertools.chain(*zipped))
        equation = "".join(flat)
        # print(f"{answer} = {equation}")
        if answer == eval_left_to_right(equation):
            return True

    return False


def main():

    # with open(".\day-07\input-sample.txt", "r") as file:
    with open(".\day-07\input.txt", "r") as file:
        input = file.read()

    total = 0
    for line in input.splitlines():
        answer = int(line.split(": ")[0])
        components = line.split(": ")[1].split(" ")

        is_valid = find_valid_equation(answer, components)
        if is_valid:
            # print(answer)
            # print(components)
            total = total + answer

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
