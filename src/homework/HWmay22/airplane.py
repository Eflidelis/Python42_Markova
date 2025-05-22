class Airplane:
    def __init__(self, model: str, max_passengers: int):
        self.model = model
        self.max_passengers = max_passengers
        self.current_passengers = 0

    def __del__(self):
        pass

    def __bool__(self):
        return True if self.current_passengers != 0 else False

    def __not__(self):
        return not self.__bool__()

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return NotImplemented

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, value: int):
        if self.current_passengers + value <= self.max_passengers:
            new_plane = Airplane(self.model, self.max_passengers)
            new_plane.current_passengers = self.current_passengers + value
            return new_plane
        else:
            raise ValueError("Превышено максимальное количество пассажиров.")

    def __sub__(self, value: int):
        if self.current_passengers - value >= 0:
            new_plane = Airplane(self.model, self.max_passengers)
            new_plane.current_passengers = self.current_passengers - value
            return new_plane
        else:
            raise ValueError("Количество пассажиров не может быть отрицательным.")

    def __iadd__(self, value: int):
        return self.__add__(value)

    def __isub__(self, value: int):
        return self.__sub__(value)

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        raise TypeError("Операция < не поддерживается для типов Airplane и " + str(type(other)))

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        raise TypeError("Операция <= не поддерживается для типов Airplane и " + str(type(other)))

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        raise TypeError("Операция > не поддерживается для типов Airplane и " + str(type(other)))

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        raise TypeError("Операция >= не поддерживается для типов Airplane и " + str(type(other)))

    def __str__(self):
        return f"{self.model} (макс. пассажиров: {self.max_passengers}, текущие пассажиры: {self.current_passengers})"
