def find_smallest_divisor(a, b):
    for i in range(2, min(a, b) + 1):
        if a % i == 0 and b % i == 0:
            return i
    return None  # если делитель не найден


def reduce_fraction():
    a = int(input("Введите первое число (числитель): "))
    b = int(input("Введите второе число (знаменатель): "))

    original_fraction = f"{a}/{b}"
    print(original_fraction, end='')

    while True:
        divisor = find_smallest_divisor(a, b)  # наименьший делитель

        if divisor is None:
            break

        # Сокращаем
        a //= divisor
        b //= divisor

        # промежуточный результат
        print(f" = {a}/{b}", end='')

    print()


reduce_fraction()
