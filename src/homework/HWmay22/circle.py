import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def __eq__(self, other):
        if isinstance(other, Circle):
            return self.radius == other.radius
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() < other.circumference()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Circle):
            return self.circumference() <= other.circumference()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Circle):
            return self.circumference() > other.circumference()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Circle):
            return self.circumference() >= other.circumference()
        return NotImplemented

    def __add__(self, value: float):
        return Circle(self.radius + value)

    def __sub__(self, value: float):
        return Circle(self.radius - value)

    def __iadd__(self, value: float):
        self.radius += value
        return self

    def __isub__(self, value: float):
        self.radius -= value
        return self

    def circumference(self):
        return 2 * math.pi * self.radius

    def __str__(self):
        return f"Circle with radius: {self.radius:.2f} and circumference: {self.circumference():.2f}"
