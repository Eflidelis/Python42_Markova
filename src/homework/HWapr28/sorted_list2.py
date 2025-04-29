def combine_unique(*lists):
    '''
    Объединяет уникальные элементы из нескольких списков

    :param lists: Списки, из которых нужно извлечь уникальные элементы
    :return: Новый список, содержащий только уникальные элементы
    '''
    combined = set()
    all_elements = set()

    for lst in lists:
        current_set = set(lst)
        unique_elements = current_set - all_elements
        combined.update(unique_elements)
        all_elements.update(current_set)

    return list(combined)


def bubble_sort(lst, ascending=True):
    '''
    Сортирует список с помощью пузырьковой сортировки

    :param lst: Список, который нужно отсортировать
    :param ascending: Параметр, определяющий порядок сортировки
    Если True, сортировка по возрастанию (указан по умолчанию), если False — по убыванию
    '''
    n = len(lst)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and lst[j] > lst[j + 1]) or (not ascending and lst[j] < lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]


def binary_search(lst, value):
    '''
    Ищет значение в отсортированном списке с помощью бинарного поиска

    :param lst: Отсортированный список, в котором нужно выполнить поиск
    :param value: Значение, которое необходимо найти в списке
    :return: Индекс найденного значения или -1, если значение не найдено
    '''
    left, right = 0, len(lst) - 1
    while left <= right:
        mid = (left + right) // 2
        if lst[mid] == value:
            return mid
        elif lst[mid] < value:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def main():
    '''
    Основная функция программы, которая выполняет объединение уникальных элементов,
    сортировку и бинарный поиск
    '''
    list1 = [15, 2, 0, 34]
    list2 = [35, 3, 25, 7]
    list3 = [9, 24, 6]
    list4 = [0, -6, 88]

    unique_combined_list = combine_unique(list1, list2, list3, list4)

    sort_order = input("Введите 'возр' для сортировки по возрастанию или 'убыв' для сортировки по убыванию: ")

    if sort_order.lower() == 'возр':
        bubble_sort(unique_combined_list, ascending=True)
    elif sort_order.lower() == 'убыв':
        bubble_sort(unique_combined_list, ascending=False)
    else:
        print("Некорректный ввод команды")

    print("Отсортированный список уникальных элементов:", unique_combined_list)

    search_value = int(input("Введите значение для поиска: "))
    result = binary_search(unique_combined_list, search_value)

    if result != -1:
        print(f"Значение {search_value} найдено по индексу {result}")
    else:
        print(f"Значение {search_value} не найдено в списке")


if __name__ == "__main__":
    main()
