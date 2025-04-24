def brackets(br_str):
    parentheses_br_count = 0
    square_br_count = 0
    curly_br_count = 0

    for br in br_str:
        if br == "(":
            parentheses_br_count += 1
        elif br == ")":
            if parentheses_br_count == 0:
                return False
            parentheses_br_count -= 1

        elif br == "[":
            square_br_count += 1
        elif br == "]":
            if square_br_count == 0:
                return False
            square_br_count -= 1

        elif br == "{":
            curly_br_count += 1
        elif br == "}":
            if curly_br_count == 0:
                return False
            curly_br_count -= 1

    return parentheses_br_count == 0 and square_br_count == 0 and curly_br_count == 0


def main():
    br_str = input("Введите строку, состоящую из скобок: ")
    result = brackets(br_str)
    print(result)


if __name__ == "__main__":
    main()
