from cwJUN3 import Sedan, Off_road_vehicle, Cargo, Car, Garage


def main():
    car = Car()
    garage = Garage()
    sedan = Sedan(price=100000, name="Лада Гранта", power=105, color="баклажан", transmission="МКПП", additional_options=3)
    off_road_vehicle = Off_road_vehicle(price=1200000, name="Jeep Grand Cherokee", power=195, color="чёрный", frame="без рамы", awd="с передним приводом", abs="ABS")
    cargo = Cargo(price=1700000, name="MAN", power=300, color="красный", tonnage=10, trailer="с прицепом", sleeping_place="со спальным местом", seats=4)

    print(sedan)
    print(off_road_vehicle)
    print(cargo)
    #print(sedan.start_engine())
    #print(off_road_vehicle.start_engine())
    #print(cargo.start_engine())



    #def drive(obj : Car):
        #print(obj.start_engine())

    #drive(cargo)

    garage.add_car(sedan)
    garage.add_car(off_road_vehicle)
    garage.add_car(cargo)

    garage.extend_car([sedan, off_road_vehicle, cargo])

    def start_all_engines(obj : Garage):
        garage.start_all_engines()

    start_all_engines(garage)

    sedan.price = 1500000
    print(f"Обновленная цена седана - {sedan.price} рублей.")

    cargo.seats = 6
    print(f"Обновленное кол-во мест в грузовике - {cargo.seats} мест.")


if __name__ == "__main__":
    main()