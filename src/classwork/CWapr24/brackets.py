def brackets(br_str):
    parentheses_br_count = 0
    square_br_count = 0
    curly_br_count = 0

    for br in br_str:
        if br == "(":
            parentheses_br_count += 1
        if br == ")" and parentheses_br_count == 1:
            parentheses_br_count -= 1
        elif br == ")" and parentheses_br_count == 0:
            return False
        if br == "[":
            square_br_count += 1
        if br == "]" and square_br_count == 1:
            square_br_count -= 1
        elif br == "]" and square_br_count == 0:
            return False
        if br == "{":
            curly_br_count += 1
        if br == "}" and curly_br_count == 1:
            curly_br_count -= 1
        elif br == "}" and curly_br_count == 0:
            return False


    if parentheses_br_count !=0 or square_br_count !=0 or curly_br_count !=0:
        return False
    if parentheses_br_count == 0 and square_br_count == 0 and curly_br_count == 0:
        return True


def main():
    br_str = input("Введите строку бла бла бла: ")
    result = brackets(br_str)
    print(result)



if __name__ == "__main__":
    main()
