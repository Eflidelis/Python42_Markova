def find_minimum(int_list):
    """
    Находит минимальное значение в списке

    :param int_list: список целых чисел
    :return:минимальное значение в списке (или None, если список пустой)
    """
    if not int_list:
        return None
    minimum = int_list[0]
    for num in int_list:
        if num < minimum:
            minimum = num
    return minimum


def is_prime(num):
    """
    Функция просто определяет, является ли число простым

    :param num: целое число
    :return: True, если число простое, иначе False
    """
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def count_primes(int_list):
    """
    Считает количество простых чисел в списке, используя функию проверки на простое число

    :param int_list: список целых чисел
    :return: количество простых чисел в списке
    """
    count = 0
    for num in int_list:
        if is_prime(num):
            count += 1
    return count


def remove_number(int_list, number):
    """
    Удаляет все вхождения заданного числа из списка

    :param int_list: список целых чисел
    :param number: число, которое нужно удалить
    :return: Количество удаленных элементов
    """
    original_length = len(int_list)
    new_list = []
    for num in int_list:
        if num != number:
            new_list.append(num)
    int_list[:] = new_list
    removed_count = original_length - len(int_list)
    return removed_count


def merge_lists(list1, list2):
    """
    Функция объединяет два списка

    :param list1: первый список
    :param list2: второй список
    :return: Объединенный список
    """
    return list1 + list2


def power_elements(int_list, power):
    """
    Возводит каждый элемент списка в заданную степень

    :param int_list: список целых чисел
    :param power: степень, в которую нужно возвести числа
    :return: новый список с числами, возведенными в данную степень
    """
    powered_list = []
    for num in int_list:
        powered_num = num ** power
        powered_list.append(powered_num)
    return powered_list


def product_of_list(int_list):
    """
    Вычисляет произведение всех элементов списка

    :param int_list: список целых чисел
    :return: произведение элементов списка
    """
    product = 1
    for num in int_list:
        product *= num
    return product


def main():
    """
    Основная функция программы: принимает от пользователя списки чисел и выбор действий с ними,
    вызывает соответствующие функции в зависимости от выбора пользователя
    :return: none
    """
    int_list = []

    while True:
        if not int_list:
            user_input = input("Введите числа, разделенные запятой: ")
            numbers = user_input.split(",")
            for num in numbers:
                cleaned_num = num.strip()
                int_value = int(cleaned_num)
                int_list.append(int_value)

        print("Выберите действие:")
        print("1 - Нахождение минимума в списке")
        print("2 - Определение количества простых чисел в списке")
        print("3 - Удаление заданного числа из списка")
        print("4 - Объединение двух списков")
        print("5 - Вычисление степени каждого числа в списке")
        print("6 - Вычисление произведения чисел списка")
        print("7 - Ввести новый список")
        print("0 - Выход")

        choice = int(input("Введите номер действия (1-8): "))

        if choice == 1:
            result = find_minimum(int_list)
            print(f"Минимум списка: {result}")
        elif choice == 2:
            result = count_primes(int_list)
            print(f"Кол-во простых чисел в списке: {result}")
        elif choice == 3:
            number_to_remove = int(input("Введите число для удаления: "))
            removed_count = remove_number(int_list, number_to_remove)
            print(f"Кол-во удаленных чисел: {removed_count}")
        elif choice == 4:
            second_input = input("Введите второй список чисел, разделенных запятой: ")
            list2 = []
            second_numbers = second_input.split(",")
            for num in second_numbers:
                cleaned_num = num.strip()
                int_value = int(cleaned_num)
                list2.append(int_value)
            merged = merge_lists(int_list, list2)
            print(f"Объединенный список: {merged}")
        elif choice == 5:
            power = int(input("Введите степень: "))
            powered_list = power_elements(int_list, power)
            print(f"Числа в степени {power}: {powered_list}")
        elif choice == 6:
            result = product_of_list(int_list)
            print(f"Произведение чисел списка: {result}")
        elif choice == 7:
            user_input = input("Введите новый список чисел, разделенных запятой: ")
            numbers = user_input.split(",")
            int_list = []
            for num in numbers:
                cleaned_num = num.strip()
                int_value = int(cleaned_num)
                int_list.append(int_value)
        elif choice == 0:
            print("До свидания!")
            break
        else:
            print("Некорректный выбор действия. Выберите номер от 1 до 8")


if __name__ == "__main__":
    main()
