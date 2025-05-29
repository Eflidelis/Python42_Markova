from roman import Roman


def main():
    roman = Roman()

    rom1 = input("Введите первое римское число: ")
    rom2 = input("Введите второе римское число: ")

    add_result = roman.add(rom1, rom2)
    print(f"Сумма: {add_result}")

    sub_result = roman.sub(rom1, rom2)
    print(f"Разность: {sub_result}")

    mul_result = roman.mul(rom1, rom2)
    print(f"Произведение: {mul_result}")

    truediv_result = roman.truediv(rom1, rom2)
    print(f"Частное: {truediv_result}")

    arabic_number = int(input("Введите арабское число для перевода в римское: "))
    roman_number = roman.arabic_to_roman(arabic_number)
    print(f"Римское число: {roman_number}")


if __name__ == "__main__":
    main()
