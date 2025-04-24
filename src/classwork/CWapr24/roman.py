def roman_to_int():
    roma_str = input("Введите число римскими цифрами: ")

    roma_dict = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    current = 0

    for char in reversed(roma_str):
        char_int = roma_dict[char]
        if char_int < current:
            total -= char_int
        else:
            total += char_int
        current = char_int
    return total


result = roman_to_int()
print(result)
