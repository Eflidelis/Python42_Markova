from circle import Circle
from complex import Complex
from airplane import Airplane
from flat import Flat


def main():

    print("Работа с окружностями:")
    circle1 = Circle(5)
    circle2 = Circle(7)

    print(circle1)
    print(circle2)
    print(circle1 == circle2)

    circle1 += 3
    print(circle1)


    print("\nРабота с комплексными числами:")
    num1 = Complex(3, 2)
    num2 = Complex(1, 4)

    print(f"num1: {num1}")
    print(f"num2: {num2}")

    sum_result = num1 + num2
    print(f"Сумма: {sum_result}")


    print("\nРабота с самолетами:")
    airplane1 = Airplane("Boeing 747", 400)
    airplane2 = Airplane("Airbus A380", 600)

    print(airplane1)
    print(airplane2)

    airplane1 += 100
    print(airplane1)

    print(airplane1 > airplane2)


    print("\nРабота с квартирами:")
    flat1 = Flat(50, 3000000)
    flat2 = Flat(70, 3500000)

    print(flat1)
    print(flat2)

    print(flat1 == flat2)
    print(flat1 < flat2)


if __name__ == "__main__":
    main()
