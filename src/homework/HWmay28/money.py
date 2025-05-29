class Currency:
    __amount = 0.0

    def __init__(self, amount: float = 0.0):
        self.__amount = amount

    def __del__(self):
        pass

    def display(self):
        return f"Сумма: {self.__amount:.2f}"


class Dollar(Currency):
    def __init__(self, dollars: float = 0.0):
        super().__init__(dollars)

    def display(self):
        return f"Сумма в долларах: {self._Currency__amount:.2f} $"


class Euro(Currency):
    def __init__(self, euros: float = 0.0):
        super().__init__(euros)

    def display(self):
        return f"Сумма в евро: {self._Currency__amount:.2f} €"


class Ruble(Currency):
    def __init__(self, rubles: float = 0.0):
        super().__init__(rubles)

    def display(self):
        return f"Сумма в рублях: {self._Currency__amount:.2f} ₽"
