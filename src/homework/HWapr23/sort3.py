def enhanced_bubble_sort(list):
    '''
    Улучшенный пузырьковый метод сортировки

    :param list: Список чисел для сортировки
    :return: Отсортированный список
    '''
    n = len(list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                swapped = True
        if not swapped:
            break
    return list


def main():
    numbers = [64, 34, 25, 12, 22, 11, 90]

    print("Исходный список:", numbers)
    sorted_numbers = enhanced_bubble_sort(numbers)
    print("Отсортированный список:", sorted_numbers)


if __name__ == "__main__":
    main()

