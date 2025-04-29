def combine_lists(*lists):
    '''
    Объединяет несколько списков в один

    :param lists: Списки, которые нужно объединить
    :return: Новый список, содержащий все элементы списков
    '''
    combined = []
    for lst in lists:
        combined.extend(lst)
    return combined


def bubble_sort(lst, ascending=True):
    '''
    Сортирует список с помощью пузырьковой сортировки

    :param lst: Список, который нужно отсортировать
    :param ascending: Параметр, определяющий порядок сортировки.
    Если True, сортировка по возрастанию (по умолчанию), если False — по убыванию.
    '''
    n = len(lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if (ascending and lst[j] > lst[j+1]) or (not ascending and lst[j] < lst[j+1]):
                lst[j], lst[j+1] = lst[j+1], lst[j]


def linear_search(lst, value):
    '''
    Ищет значение в списке с помощью линейного поиска

    :param lst: Список, в котором нужно выполнить поиск
    :param value: Значение, которое необходимо найти в списке
    :return: Индекс найденного значения или -1, если значение не найдено
    '''
    for index, item in enumerate(lst):
        if item == value:
            return index
    return -1


def main():
    '''
    Основная функция программы, которая выполняет объединение списков,
    сортировку и поиск значения
    '''
    list1 = [5, 2, 9, 1]
    list2 = [3, 6, 4]
    list3 = [8, 7]
    list4 = [10, 0]

    combined_list = combine_lists(list1, list2, list3, list4)

    sort_order = input("Введите 'возр' для сортировки по возрастанию или 'убывc' для сортировки по убыванию: ")

    if sort_order.lower() == 'возр':
        bubble_sort(combined_list, ascending=True)
    elif sort_order.lower() == 'убыв':
        bubble_sort(combined_list, ascending=False)
    else:
        print("Некорректный ввод команды")

    print("Отсортированный список:", combined_list)

    search_value = int(input("Введите значение для поиска: "))
    result = linear_search(combined_list, search_value)

    if result != -1:
        print(f"Значение {search_value} найдено по индексу {result}")
    else:
        print(f"Значение {search_value} не найдено в списке")


if __name__ == "__main__":
    main()
