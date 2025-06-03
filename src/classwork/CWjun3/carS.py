from cwJUN3 import Sedan, Off_road_vehicle, Cargo


def main():
    print("Выберите тип автомобиля:")
    print("1. Седан")
    print("2. Внедорожник")
    print("3. Грузовик")

    choice = input("Введите номер типа автомобиля (1-3): ")

    if choice == '1':
        # Предопределенные характеристики для Седана
        default_name = "Лада Гранта"
        default_color = "баклажан"
        default_power = 105
        default_transmission = "МКПП"
        default_additional_options = 3

        print("Предопределенные характеристики для седана:")
        print(f"Название: {default_name}, Цвет: {default_color}, Мощность: {default_power} л.с., "
              f"Трансмиссия: {default_transmission}, Дополнительные опции: {default_additional_options}")

        # Ввод характеристик от пользователя
        name = input(
            "Введите название седана (или нажмите Enter для использования предопределенного): ") or default_name
        color = input("Введите цвет седана (или нажмите Enter для использования предопределенного): ") or default_color
        power = input("Введите мощность седана (л.с.) (или нажмите Enter для использования предопределенного): ")
        power = int(power) if power else default_power
        transmission = input(
            "Введите тип трансмиссии (АКПП/МКПП) (или нажмите Enter для использования предопределенного): ") or default_transmission
        additional_options = input(
            "Введите количество дополнительных опций (или нажмите Enter для использования предопределенного): ")
        additional_options = int(additional_options) if additional_options else default_additional_options

        price = 100000 + additional_options * 5000  # Доплата за дополнительные опции
        sedan = Sedan(price=price, name=name, power=power, color=color, transmission=transmission,
                      additional_options=additional_options)
        print(sedan)

    elif choice == '2':
        # Предопределенные характеристики для Внедорожника
        default_name = "Jeep Grand Cherokee"
        default_color = "чёрный"
        default_power = 195
        default_frame = "без рамы"
        default_awd = "с передним приводом"
        default_abs = "ABS"

        print("Предопределенные характеристики для внедорожника:")
        print(f"Название: {default_name}, Цвет: {default_color}, Мощность: {default_power} л.с., "
              f"Рама: {default_frame}, Привод: {default_awd}, ABS: {default_abs}")

        # Ввод характеристик от пользователя
        name = input(
            "Введите название внедорожника (или нажмите Enter для использования предопределенного): ") or default_name
        color = input(
            "Введите цвет внедорожника (или нажмите Enter для использования предопределенного): ") or default_color
        power = input("Введите мощность внедорожника (л.с.) (или нажмите Enter для использования предопределенного): ")
        power = int(power) if power else default_power
        frame = input(
            "Есть ли рама? (да/нет) (или нажмите Enter для использования предопределенного): ") or default_frame
        awd = input(
            "Какой привод? (передний/задний/полный) (или нажмите Enter для использования предопределенного): ") or default_awd
        abs = input("Есть ли ABS? (да/нет) (или нажмите Enter для использования предопределенного): ") or default_abs

        price = 1200000
        off_road_vehicle = Off_road_vehicle(price=price, name=name, power=power, color=color, frame=frame, awd=awd,
                                            abs=abs)
        print(off_road_vehicle)

    elif choice == '3':
        # Предопределенные характеристики для Грузовика
        default_name = "MAN"
        default_color = "красный"
        default_power = 300
        default_tonnage = 10
        default_trailer = "с прицепом"
        default_sleeping_place = "со спальным местом"
        default_seats = 4

        print("Предопределенные характеристики для грузовика:")
        print(f"Название: {default_name}, Цвет: {default_color}, Мощность: {default_power} л.с., "
              f"Тоннаж: {default_tonnage} т, Прицеп: {default_trailer}, Спальное место: {default_sleeping_place}, Места: {default_seats}")

        # Ввод характеристик от пользователя
        name = input(
            "Введите название грузовика (или нажмите Enter для использования предопределенного): ") or default_name
        color = input(
            "Введите цвет грузовика (или нажмите Enter для использования предопределенного): ") or default_color
        power = input("Введите мощность грузовика (л.с.) (или нажмите Enter для использования предопределенного): ")
        power = int(power) if power else default_power
        tonnage = input("Введите тоннаж грузовика (т) (или нажмите Enter для использования предопределенного): ")
        tonnage = int(tonnage) if tonnage else default_tonnage
        trailer = input(
            "Есть ли прицеп? (да/нет) (или нажмите Enter для использования предопределенного): ") or default_trailer
        sleeping_place = input(
            "Есть ли спальное место? (да/нет) (или нажмите Enter для использования предопределенного): ") or default_sleeping_place
        seats = input("Введите количество мест (или нажмите Enter для использования предопределенного): ")
        seats = int(seats) if seats else default_seats

        price = 1700000
        cargo = Cargo(price=price, name=name, power=power, color=color, tonnage=tonnage, trailer=trailer,
                      sleeping_place=sleeping_place, seats=seats)
        print(cargo)

    else:
        print("Неверный выбор. Пожалуйста, выберите номер от 1 до 3.")

if __name__ == "__main__":
    main()