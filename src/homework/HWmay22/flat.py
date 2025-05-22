class Flat:
    def __init__(self, area: float, price: float):
        self.area = area
        self.price = price

    def __eq__(self, other):
        if isinstance(other, Flat):
            return self.area == other.area
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __lt__(self, other):
        if isinstance(other, Flat):
            return self.price < other.price
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Flat):
            return self.price <= other.price
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Flat):
            return self.price > other.price
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Flat):
            return self.price >= other.price
        return NotImplemented

    def __str__(self):
        return f"Квартира: площадь {self.area} м², цена {self.price} руб."
