def find_min(numbers):
    """
    Находит минимальный элемент в списке чисел

    :param numbers: cписок целых чисел
    :return: Минимальное число из списка
    """
    return min(numbers) if numbers else None


def find_max(numbers):
    """
    Находит максимальный элемент в списке чисел

    :param numbers: Список целых чисел
    :return: Максимальный элемент из списка чичел
    """
    return max(numbers) if numbers else None


def count_negatives(numbers):
    """
    Считает количество отрицательных чисел в списке

    :param numbers: Список целых чисел
    :return: Количество отрицательных чисел
    """
    return sum(1 for num in numbers if num < 0)


def count_positives(numbers):
    """
    Считает количество положительных чисел в списке

    :param numbers: Список целых чисел
    :return: Количество положительных чисел
    """
    return sum(1 for num in numbers if num > 0)


def count_zeros(numbers):
    """
    Считает количество нулей в списке

    :param numbers: Список целых чисел
    :return: Количество нулей
    """
    return numbers.count(0)


def main():
    """
    Основная функция программы, которая управляет вводом чисел пользователем и выбором опций

    :return: none
    """
    numbers = []

    while True:
        num = int(input("Введите целое число (или -1 для завершения ввода): "))
        if num == -1:
            break
        numbers.append(num)

    while True:
        print("\nМеню:")
        print("1. Найти минимальное число")
        print("2. Найти максимальное число")
        print("3. Посчитать количество отрицательных чисел")
        print("4. Посчитать количество положительных чисел")
        print("5. Посчитать количество нулей")
        print("6. Выйти из программы")

        choice = input("Выберите опцию (1-6): ")

        if choice == '1':
            print("Минимальное число:", find_min(numbers))
        elif choice == '2':
            print("Максимальное число:", find_max(numbers))
        elif choice == '3':
            print("Количество отрицательных чисел:", count_negatives(numbers))
        elif choice == '4':
            print("Количество положительных чисел:", count_positives(numbers))
        elif choice == '5':
            print("Количество нулей:", count_zeros(numbers))
        elif choice == '6':
            print("До свидания!")
            break
        else:
            print("Некорректный выбор. Выберите опцию от 1 до 6.")


if __name__ == "__main__":
    main()
