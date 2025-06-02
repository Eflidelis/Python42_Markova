class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Shape:
    def area(self):
        raise NotImplementedError("Этот метод должен быть написан в других классах.")


class Square(Shape, Position):
    def __init__(self, x, y, side_length):
        Position.__init__(self, x, y)
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2


class RectangleShape(Shape, Position):
    def __init__(self, x, y, width, height):
        Position.__init__(self, x, y)
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class CircleShape(Shape, Position):
    def __init__(self, center_x, center_y, radius):
        Position.__init__(self, center_x, center_y)
        self.radius = radius

    def area(self):
        return 3.1415 * self.radius ** 2


class Ellipse(Shape, Position):
    def __init__(self, x, y, width, height):
        Position.__init__(self, x, y)
        self.width = width
        self.height = height

    def area(self):
        return 3.1415 * (self.width / 2) * (self.height / 2)
