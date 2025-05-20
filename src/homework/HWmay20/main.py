from book_book import Book
from car_car import Car
from stadium_stadium import Stadium


def main():
    while True:
        print("\nВыберите действие:")
        print("1. Работа с книгой")
        print("2. Работа с машиной")
        print("3. Работа со стадионом")
        print("4. Выход")

        choice = input("Введите номер действия (1/2/3/4): ")

        if choice == '1':
            book = Book()
            print("\nИсходные данные о книге:")
            print(book)

            title = input("Введите название книги (оставьте пустым для сохранения текущего значения): ")
            autor = input("Введите автора книги (оставьте пустым для сохранения текущего значения): ")
            genre = input("Введите жанр книги (оставьте пустым для сохранения текущего значения): ")
            year = input("Введите год издания (оставьте пустым для сохранения текущего значения): ")
            publisher = input("Введите издательство (оставьте пустым для сохранения текущего значения): ")
            price = input("Введите цену (оставьте пустым для сохранения текущего значения): ")

            book.input_data(
                title=title if title else None,
                autor=autor if autor else None,
                genre=genre if genre else None,
                year=int(year) if year.isdigit() else None,
                publisher=publisher if publisher else None,
                price=float(price) if price.replace('.', '', 1).isdigit() else None
            )

            print("\nОбновленные данные о книге:")
            print(book)

        elif choice == '2':
            car = Car()
            print("\nИсходные данные о машине:")
            print(car)

            model = input("Введите модель машины (оставьте пустым для сохранения текущего значения): ")
            year = input("Введите год выпуска (оставьте пустым для сохранения текущего значения): ")
            manufacturer = input("Введите производителя (оставьте пустым для сохранения текущего значения): ")
            engine_volume = input("Введите объем двигателя (оставьте пустым для сохранения текущего значения): ")
            color = input("Введите цвет машины (оставьте пустым для сохранения текущего значения): ")
            price = input("Введите цену (оставьте пустым для сохранения текущего значения): ")

            car.input_data(
                model=model if model else None,
                year=int(year) if year.isdigit() else None,
                manufacturer=manufacturer if manufacturer else None,
                engine_volume=float(engine_volume) if engine_volume.replace('.', '', 1).isdigit() else None,
                color=color if color else None,
                price=float(price) if price.replace('.', '', 1).isdigit() else None
            )

            print("\nОбновлённые данные о машине:")
            print(car)

        elif choice == '3':
            stadium = Stadium()
            print("\nИсходные данные о стадионе:")
            print(stadium)

            name = input("Введите название стадиона (оставьте пустым для сохранения текущего значения): ")
            opening_date = input("Введите дату открытия (оставьте пустым для сохранения текущего значения): ")
            country = input("Введите страну (оставьте пустым для сохранения текущего значения): ")
            city = input("Введите город (оставьте пустым для сохранения текущего значения): ")
            capacity = input("Введите вместимость (оставьте пустым для сохранения текущего значения): ")

            stadium.input_data(
                name=name if name else None,
                opening_date=opening_date if opening_date else None,
                country=country if country else None,
                city=city if city else None,
                capacity=int(capacity) if capacity.isdigit() and int(capacity) > 0 else None
            )

            print("\nОбновленные данные о стадионе:")
            print(stadium)

        elif choice == '4':
            print("До свидания!")
            break

        else:
            print("Некорректный ввод. Введите 1, 2, 3 или 4")


if __name__ == "__main__":
    main()
