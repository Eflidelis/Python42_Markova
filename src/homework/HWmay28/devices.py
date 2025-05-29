class Device:
    __name = str()
    __power = 0

    def __init__(self, name: str = "", power: int = 0):
        self.__name = name
        self.__power = power

    def __del__(self):
        pass

    def display(self):
        return f"Устройство: {self.__name}, Мощность: {self.__power} Вт"


class KitchenDevice(Device):
    def __init__(self, name: str = "", power: int = 0):
        super().__init__(name, power)


class Blender(KitchenDevice):
    __speed_levels = 0

    def __init__(self, name: str = "", power: int = 0, speed_levels: int = 0):
        super().__init__(name, power)
        self.__speed_levels = speed_levels

    def __del__(self):
        pass

    def blend(self):
        return f"{self._Device__name} смешивает на {self.__speed_levels} уровнях скорости."


class MeatGrinder(KitchenDevice):
    __capacity = 0

    def __init__(self, name: str = "", power: int = 0, capacity: int = 0):
        super().__init__(name, power)
        self.__capacity = capacity

    def __del__(self):
        pass

    def grind(self):
        return f"{self._Device__name} измельчает до {self.__capacity} кг мяса."
