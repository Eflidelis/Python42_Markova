class Roman:
    roman_nums = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    def __init__(self, roman=None):
        self.roman = roman
        if roman:
            self.__value = self.roman_to_int(roman)

    def roman_to_int(self, roma_str):
        total = 0
        current = 0
        for char in reversed(roma_str):
            char_int = self.roman_nums[char]
            if char_int < current:
                total -= char_int
            else:
                total += char_int
            current = char_int
        return total

    def arabic_to_roman(self, arabic):
        if arabic < 1 or arabic > 3999:
            return "Число должно быть в диапазоне от 1 до 3999"

        roman_numerals = {value: key for key, value in self.roman_nums.items()}

        roman_value = ""
        for value in sorted(roman_numerals.keys(), reverse=True):
            while arabic >= value:
                roman_value += roman_numerals[value]
                arabic -= value

        return roman_value

    def add(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)
        return num1 + num2

    def sub(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)
        return num1 - num2

    def mul(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)
        return num1 * num2

    def truediv(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)
        return num1 / num2
