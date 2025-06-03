from cwJUN3 import Sedan, Off_road_vehicle, Cargo


def main():
    sedan = Sedan(price=100000, name="Лада Гранта", power=105, color="баклажан", transmission="МКПП", additional_options=3)
    off_road_vehicle = Off_road_vehicle(price=1200000, name="Jeep Grand Cherokee", power=195, color="чёрный", frame="без рамы", awd="с передним приводом", abs="ABS")
    cargo = Cargo(price=1700000, name="MAN", power=300, color="красный", tonnage=10, trailer="с прицепом", sleeping_place="со спальным местом", seats=4)

    print(sedan)
    print(off_road_vehicle)
    print(cargo)

    sedan.price = 1500000
    print(f"Обновленная цена седана - {sedan.price} рублей.")

    cargo.seats = 6
    print(f"Обновленное кол-во мест в грузовике - {cargo.seats} мест.")


if __name__ == "__main__":
    main()