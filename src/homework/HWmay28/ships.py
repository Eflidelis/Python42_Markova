class Ship:
    __name = str()
    __tonnage = 0

    def __init__(self, name: str = "", tonnage: int = 0):
        self.__name = name
        self.__tonnage = tonnage

    def __del__(self):
        pass

    def display(self):
        return f"Корабль: {self.__name}, Водоизмещение: {self.__tonnage} тонн"


class NavalShip(Ship):
    def __init__(self, name: str = "", tonnage: int = 0):
        super().__init__(name, tonnage)


class Frigate(NavalShip):
    __armament = str()

    def __init__(self, name: str = "", tonnage: int = 0, armament: str = ""):
        super().__init__(name, tonnage)
        self.__armament = armament

    def __del__(self):
        pass

    def engage(self):
        return f"{self._Ship__name} с вооружением {self.__armament} вступает в бой."


class Destroyer(NavalShip):
    __speed = 0

    def __init__(self, name: str = "", tonnage: int = 0, speed: int = 0):
        super().__init__(name, tonnage)
        self.__speed = speed

    def __del__(self):
        pass

    def patrol(self):
        return f"{self._Ship__name} патрулирует на скорости {self.__speed} узлов."


class Cruiser(NavalShip):
    __missile_capacity = 0

    def __init__(self, name: str = "", tonnage: int = 0, missile_capacity: int = 0):
        super().__init__(name, tonnage)
        self.__missile_capacity = missile_capacity

    def __del__(self):
        pass

    def launch_missiles(self):
        return f"{self._Ship__name} запускает {self.__missile_capacity} ракет."
