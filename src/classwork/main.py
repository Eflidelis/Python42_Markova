from CWmay22 import Roman


def main():
    num1 = input("Введите первое римское число: ")
    num2 = input("Введите первое римское число: ")

    roman = Roman(num1)

    rom1 = roman.roman_to_int(num1)
    rom2 = roman.roman_to_int(num2)

    add_result = roman.__add__(rom1, rom2)
    print(add_result)

    sub_result = roman.__sub__(rom1, rom2)
    print(sub_result)

    mul_result = roman.__sub__(rom1, rom2)
    print(mul_result)

    truediv_result = roman.__truediv__(rom1, rom2)
    print(truediv_result)


if __name__ == "__main__":
    main()




