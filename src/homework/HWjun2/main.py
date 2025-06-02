from shapes import Square, RectangleShape, CircleShape, Ellipse


def main():
    shapes = [
        Square(0, 0, 5),
        RectangleShape(1, 1, 10, 5),
        CircleShape(5, 5, 3),
        Ellipse(2, 2, 4, 2)
    ]

    for shape in shapes:
        print(f"{shape.__class__.__name__}: Площадь = {shape.area()}")


if __name__ == "__main__":
    main()
