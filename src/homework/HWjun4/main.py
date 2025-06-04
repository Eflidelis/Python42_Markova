from car import Sedan, Off_road_vehicle, Cargo


def calculate_price(base_price, power, additional_options):
    power_price = (power - 100) * 1000
    options_price = additional_options * 5000
    return base_price + power_price + options_price


def main():
    print("Выберите тип автомобиля:")
    print("1. Седан")
    print("2. Внедорожник")
    print("3. Грузовик")

    choice = input("Введите номер типа автомобиля (1-3): ")

    sedan_models = [("Лада Гранта", 500000), ("Toyota Camry", 1500000), ("Volkswagen Polo", 900000)]
    off_road_models = [("Jeep Grand Cherokee", 3000000), ("Toyota Land Cruiser", 4000000), ("Nissan Patrol", 3500000)]
    cargo_models = [("MAN", 2000000), ("Scania", 2500000), ("Volvo", 2200000)]

    colors = ["красный", "черный", "белый"]
    powers = [105, 195, 300]
    transmissions = ["АКПП", "МКПП"]

    if choice == '1':
        print("Доступные модели седанов:")
        for i, (model, base_price) in enumerate(sedan_models, start=1):
            print(f"{i}. {model} - базовая цена: {base_price} рублей")
        model_choice = int(input("Выберите номер модели седана: ")) - 1
        model, base_price = sedan_models[model_choice]

        print("Доступные цвета:")
        for i, color in enumerate(colors, start=1):
            print(f"{i}. {color}")
        color_choice = int(input("Выберите номер цвета: ")) - 1
        color = colors[color_choice]

        print("Доступные мощности: ")
        for i, power in enumerate(powers[:2], start=1):
            print(f"{i}. {power} л.с.")
        power_choice = int(input("Выберите номер мощности: ")) - 1
        power = powers[power_choice]

        print("Доступные трансмиссии:")
        for i, transmission in enumerate(transmissions, start=1):
            print(f"{i}. {transmission}")
        transmission_choice = int(input("Выберите номер трансмиссии: ")) - 1
        transmission = transmissions[transmission_choice]

        additional_options = int(input("Введите количество дополнительных опций: "))

        price = calculate_price(base_price, power, additional_options)
        sedan = Sedan(price=price, name=model, power=power, color=color, transmission=transmission, additional_options=additional_options)

    elif choice == '2':
        print("Доступные модели внедорожников:")
        for i, (model, base_price) in enumerate(off_road_models, start=1):
            print(f"{i}. {model} - базовая цена: {base_price} рублей")
        model_choice = int(input("Выберите номер модели внедорожника: ")) - 1
        model, base_price = off_road_models[model_choice]

        print("Доступные цвета:")
        for i, color in enumerate(colors, start=1):
            print(f"{i}. {color}")
        color_choice = int(input("Выберите номер цвета: ")) - 1
        color = colors[color_choice]

        print("Доступные мощности: ")
        for i, power in enumerate(powers[1:], start=1):
            print(f"{i}. {power} л.с.")
        power_choice = int(input("Выберите номер мощности: ")) - 1
        power = powers[power_choice + 1]

        print("Доступные трансмиссии:")
        for i, transmission in enumerate(transmissions, start=1):
            print(f"{i}. {transmission}")
        transmission_choice = int(input("Выберите номер трансмиссии: ")) - 1
        transmission = transmissions[transmission_choice]

        frame = input("Есть ли рама? (да/нет): ")
        awd = input("Какой привод? (передний/задний/полный): ")
        abs = input("Есть ли ABS? (да/нет): ")

        price = base_price
        off_road_vehicle = Off_road_vehicle(price=price, name=model, power=power, color=color, frame=frame, awd=awd, abs=abs)

    elif choice == '3':
        print("Доступные модели грузовиков:")
        for i, (model, base_price) in enumerate(cargo_models, start=1):
            print(f"{i}. {model} - базовая цена: {base_price} рублей")
        model_choice = int(input("Выберите номер модели грузовика: ")) - 1
        model, base_price = cargo_models[model_choice]

        print("Доступные цвета:")
        for i, color in enumerate(colors, start=1):
            print(f"{i}. {color}")
        color_choice = int(input("Выберите номер цвета: ")) - 1
        color = colors[color_choice]

        print("Доступные мощности: ")
        for i, power in enumerate(powers[2:], start=1):
            print(f"{i}. {power} л.с.")
        power_choice = int(input("Выберите номер мощности: ")) - 1
        power = powers[power_choice + 2]

        tonnage = int(input("Введите тоннаж грузовика (т): "))
        trailer = input("Есть ли прицеп? (да/нет): ")
        sleeping_place = input("Есть ли спальное место? (да/нет): ")
        seats = int(input("Введите количество мест: "))

        price = base_price
        cargo = Cargo(price=price, name=model, power=power, color=color, tonnage=tonnage, trailer=trailer, sleeping_place=sleeping_place, seats=seats)

    else:
        print("Неверный выбор. Пожалуйста, выберите номер от 1 до 3.")
        return

    print("\nВыбранные характеристики:")
    print("Тип автомобиля:", "Седан" if choice == '1' else "Внедорожник" if choice == '2' else "Грузовик")
    print("Модель:", model)
    print("Цвет:", color)
    print("Мощность:", power, "л.с.")
    if choice == '1':
        print("Трансмиссия:", transmission)
        print("Дополнительные опции:", additional_options)
    elif choice == '2':
        print("Рама:", frame)
        print("Привод:", awd)
        print("ABS:", abs)
    elif choice == '3':
        print("Тоннаж:", tonnage, "т")
        print("Прицеп:", trailer)
        print("Спальное место:", sleeping_place)
        print("Количество мест:", seats)

    print("Итоговая цена:", sedan.price if choice == '1' else off_road_vehicle.price if choice == '2' else cargo.price)


if __name__ == "__main__":
    main()
