def bubble_sort(lst):
    '''
    Сортирует список с использованием пузырькового метода

    :param lst: Список чисел для сортировки
    :return: Отсортированный список
    '''
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


def selection_sort(lst):
    '''
    Сортирует список с использованием метода выборки

    :param lst: Список чисел для сортировки
    :return: Отсортированный список
    '''
    n = len(lst)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if lst[j] < lst[min_index]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def insertion_sort(lst):
    '''
    Сортирует список с использованием метода вставками

    :param lst: Список чисел для сортировки
    :return: Отсортированный список
    '''
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def custom_sort(numbers, sort_function):
    '''
    Выполняет пользовательскую сортировку списка, используя заданную функцию сортировки

    :param numbers: Список чисел для сортировки
    :param sort_function: функция сортировки, которая будет применена к части списка
    :return: отсортированный список с перевернутой оставшейся частью
    '''
    if not numbers:
        return []

    mean_value = sum(numbers) / len(numbers)
    n = len(numbers)

    if mean_value > 0:
        to_sort = numbers[:2 * n // 3]
    else:
        to_sort = numbers[:n // 3]

    sorted_part = sort_function(to_sort)

    remaining_part = numbers[2 * n // 3:] if mean_value > 0 else numbers[n // 3:]
    reversed_part = remaining_part[::-1]

    result = sorted_part + reversed_part
    return result


def main():
    '''
    Главная функция программы, которая запрашивает у пользователя выбор метода сортировки
    и выводит отсортированный список
    '''
    numbers = [3, -1, 4, 1, 5, -9, 2, 6, 5]
    print("Исходный список:", numbers)

    print("\nВыберите способ сортировки:")
    print("1. Пузырьковая сортировка")
    print("2. Сортировка выборкой")
    print("3. Сортировка вставками")

    choice = input("Введите номер способа сортировки (1-3): ")

    if choice == '1':
        sorted_list = custom_sort(numbers, bubble_sort)
    elif choice == '2':
        sorted_list = custom_sort(numbers, selection_sort)
    elif choice == '3':
        sorted_list = custom_sort(numbers, insertion_sort)
    else:
        print("Некорректный выбор")
        return

    print("Отсортированный список:", sorted_list)


if __name__ == "__main__":
    main()
