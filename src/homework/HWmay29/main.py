from bit_calc import BitwiseOperations


def main():
    x = int(input("Введите первое число (x): "))
    y = int(input("Введите второе число (y): "))

    bit_ops = BitwiseOperations()

    sum_result = bit_ops.add(x, y)
    sub_result = bit_ops.subtract(x, y)

    print(f"Результат сложения: {sum_result}")
    print(f"Результат вычитания: {sub_result}")


if __name__ == "__main__":
    main()
