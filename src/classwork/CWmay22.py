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

    def __init__(self, roman):
        self.__roman = roman
        self.__value = self.roman_to_int(roman)

    def roman_to_int(self, roman):
        total = 0
        current = 0
        for char in reversed(roman):
            char_int = self.roman_nums[char]
            if char_int < current:
                total -= char_int
            else:
                total += char_int
            current = char_int
        return total

    def __del__(self):
        pass

    def __add__(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)

        return self.roman_to_int(num1 + num2)

    def __sub__(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)

        return self.roman_to_int(num1 - num2)

    def __mul__(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)

        return self.roman_to_int(num1 * num2)

    def __truediv__(self, rom1, rom2):
        num1 = self.roman_to_int(rom1)
        num2 = self.roman_to_int(rom2)

        return self.roman_to_int(num1 / num2)

