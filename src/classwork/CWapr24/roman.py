def roman_to_int():
    roma_str = input("Введите число римскими цифрами: ")

    total = 0
    current = 0

    for char in roma_str:
        if char == "I":
            char = 1
            current = 1
        elif char == "V":
            char = 5
            current = 5
        elif char == "X":
            char = 10
            current = 10
        elif char == "L":
            char = 50
            current = 50
        elif char == "C":
            char = 100
            current = 100


    for char in reversed(roma_str):
        char_int = current
        if char < current:
            total -= char_int
        else:
            total += char_int
        current = char_int
    return total


result = roman_to_int()
print(result)
