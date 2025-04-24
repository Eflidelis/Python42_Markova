def bubble_sort(list, ascending=True):
    '''
    Сортирует список с использованием пузырькового метода

    :param list: Список чисел для сортировки
    :param ascending: Указывает порядок сортировки (по возрастанию или убыванию, по умолчанию - по возрастанию)
    :return: Отсортированный список
    '''
    n = len(list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if (ascending and list[j] > list[j + 1]) or (not ascending and list[j] < list[j + 1]):
                list[j], list[j + 1] = list[j + 1], list[j]
    return list


def main():
    grades = []

    print("Введите 10 оценок студента от 1 до 12: ")
    while len(grades) < 10:
        try:
            grade = int(input(f"Оценка {len(grades) + 1}: "))
            if 1 <= grade <= 12:
                grades.append(grade)
            else:
                print("Оценка должна быть от 1 до 12")
        except ValueError:
            print("Введите целое число")

    while True:
        print("\nМеню:")
        print("1. Вывод оценок")
        print("2. Пересдача экзамена")
        print("3. Проверка стипендии")
        print("4. Вывод отсортированного списка оценок")
        print("5. Выход")

        choice = input("Выберите действие (1-5): ")

        if choice == '1':
            print("Оценки:", grades)

        elif choice == '2':
            index = int(input("Введите номер оценки для пересдачи (1-10): ")) - 1
            if 0 <= index < len(grades):
                new_grade = int(input("Введите новую оценку (от 1 до 12): "))
                if 1 <= new_grade <= 12:
                    grades[index] = new_grade
                    print("Оценка обновлена.")
                else:
                    print("Оценка должна быть от 1 до 12")
            else:
                print("Некорректный номер оценки")

        elif choice == '3':
            average = sum(grades) / len(grades)
            if average >= 10.7:
                print("Стипендия будет начислена")
            else:
                print("Стипендии не будет")

        elif choice == '4':
            order = input("Сортировать по возр или убыв? (введите 'возр' или 'убыв') ")
            if order == 'возр':
                sorted_grades = bubble_sort(grades, ascending=True)
                print("Отсортированные оценки по возрастанию:", sorted_grades)
            elif order == 'убыв':
                sorted_grades = bubble_sort(grades, ascending=False)
                print("Отсортированные оценки по убыванию:", sorted_grades)
            else:
                print("Некорректный ввод")

        elif choice == '5':
            print("До свидания!")
            break

        else:
            print("Некорректный выбор. Выберите действие от 1 до 5")


if __name__ == "__main__":
    main()
