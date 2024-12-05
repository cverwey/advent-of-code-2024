def page_valid(page, rules):
    for rule in rules:
        reduced_page = [p for p in page if p in rule]
        if len(reduced_page) == 2 and reduced_page != rule:
            return False
    return True


def fix_invalid_page(page, rules, iter=1000):

    # prevent infinite loop
    if iter == 0:
        return False

    for rule in rules:
        reduced_page = [p for p in page if p in rule]
        if len(reduced_page) == 2 and reduced_page != rule:
            page[page.index(rule[0])] = rule[1]
            page[page.index(rule[1])] = rule[0]
            return fix_invalid_page(page, rules, iter - 1)

    return page


def main():

    rules = []
    pages = []

    reached_blank_line = False
    # with open(".\day-05\input-sample.txt", "r") as file:
    with open(".\day-05\input.txt", "r") as file:
        for line in file:

            if line.strip() == "":
                reached_blank_line = True
                continue

            if reached_blank_line:
                page = list(map(int, line.strip().split(",")))
                pages.append(page)
            else:
                rule = list(map(int, line.strip().split("|")))
                rules.append(rule)

    total = 0
    for page in pages:
        if not page_valid(page, rules):
            fixed_page = fix_invalid_page(page, rules)
            total = total + page[len(fixed_page) // 2]

    print(f"Total: {total}")


if __name__ == "__main__":
    main()
