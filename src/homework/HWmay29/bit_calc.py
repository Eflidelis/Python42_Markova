class BitwiseOperations:

    def __init__(self, x : int = 0, y : int = 0):
        self.__x = x
        self.__y = y

    def __del__(self):
        pass

    def add(self, x, y):
        while y != 0:
            carry = x & y  # логическое И (получаем перенос)
            x = x ^ y      # логическое ИЛИ (получили новый x)
            y = carry << 1 # Перенос переноса на один бит влево (получили новый y)
        return x

    def subtract(self, x, y):
        while y != 0:
            borrow = (~x) & y  # логическое И, где x инвертирован (получили заем)
            x = x ^ y          # логическое ИЛИ (получили новый x)
            y = borrow << 1    # переносим заём на 1 бит влево (получили новый y)
        return x