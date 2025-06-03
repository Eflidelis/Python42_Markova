from cwJUN3 import Sedan, Off_road_vehicle, Cargo

def main():
    sedan = Sedan(price=100000, name="Лада Гранта", power=105, color="баклажан", transmission="МКПП", additional_options=3)
    off_road_vehicle = Off_road_vehicle(price=1200000, name="Jeep Grand Cherokee", power=195, color="чёрный", frame="без рамы", awd="с передним приводом", abs="ABS")
    cargo = Cargo(price=1700000, name="MAN", power=300, color="красный", tonnage=10, trailer="с прицепом", sleeping_place="со спальным местом", seats=4)

    print("Выберите тип автомобиля:")
    print("1. Седан")
    print("2. Внедорожник")
    print("3. Грузовик")

    choice = input("Введите номер типа автомобиля (1-3): ")

    if choice == '1':

        print("Предопределенные характеристики для седана:")
        print(f"Название: {sedan.name}, Цвет: {sedan.color}, Мощность: {sedan.power} л.с., "
          f"Трансмиссия: {sedan.transmission}, Дополнительные опции: {sedan.additional_options}")