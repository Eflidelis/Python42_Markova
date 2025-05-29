from devices import Blender, MeatGrinder
from ships import Frigate, Destroyer, Cruiser
from money import Dollar, Euro, Ruble


def main():
    # Использование классов устройств
    blender = Blender("Мощный блендер", 500, 5)
    print(blender.display())
    print(blender.blend())

    meat_grinder = MeatGrinder("Мясорубка", 300, 2)
    print(meat_grinder.display())
    print(meat_grinder.grind())

    # Использование классов кораблей
    frigate = Frigate("Фрегат-1", 3000, "ракетные установки")
    print(frigate.display())
    print(frigate.engage())

    destroyer = Destroyer("Эсминец-1", 2500, 30)
    print(destroyer.display())
    print(destroyer.patrol())

    cruiser = Cruiser("Крейсер-1", 4000, 20)
    print(cruiser.display())
    print(cruiser.launch_missiles())

    # Использование класса Money
    dollar = Dollar(10.50)
    print(dollar.display())

    euro = Euro(20.75)
    print(euro.display())

    ruble = Ruble(1500.25)
    print(ruble.display())


if __name__ == "__main__":
    main()
