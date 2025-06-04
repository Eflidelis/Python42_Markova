class Car():
    __price = 0
    __name = str()
    __color = str()
    __power = 0

    def __init__(self, price: int = 0, name: str = "", power: int = 0, color: str = ""):
        self.__name = name
        self.__power = power
        self.__color = color
        self.__price = price

    def __del__(self):
        pass

    def __str__(self):
        return f"Автомобиль {self.__name} цвета {self.__color} мощностью {self.__power} л.с. стоит {self.__price} рублей"

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Цена не может быть отрицательной")
        self.__price = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, value):
        self.__color = value

    @property
    def power(self):
        return self.__power

    @power.setter
    def power(self, value):
        if value < 0:
            raise ValueError("Мощность не может быть отрицательной.")
        self.__power = value


class Sedan(Car):
    __transmission = str()
    __additional_options = 0

    def __init__(self, price: int = 0, name: str = "", power: int = 0, color: str = "", transmission: str = "", additional_options: int = 0):
        super().__init__(price, name, power, color)
        self.__transmission = transmission
        self.__additional_options = additional_options

    def __del__(self):
        pass

    def __str__(self):
        return super().__str__() + f", класс - СЕДАН, трансмиссия: {self.__transmission}, доп.опций: {self.__additional_options} штук."

    @property
    def transmission(self):
        return self.__transmission

    @transmission.setter
    def transmission(self, value):
        self.__transmission = value

    @property
    def additional_options(self):
        return self.__additional_options

    @additional_options.setter
    def additional_options(self, value):
        if value < 0:
            raise ValueError("Кол-во опций не может быть отрицательным.")
        self.__additional_options = value


class Off_road_vehicle(Car):
    __frame = str()
    __awd = str()
    __abs = str()

    def __init__(self, price: int = 0, name: str = "", power: int = 0, color: str = "", frame: str = "",
                 awd: str = "", abs: str = ""):
        super().__init__(price, name, power, color)
        self.__frame = frame
        self.__awd = awd
        self.__abs = abs

    def __del__(self):
        pass

    def __str__(self):
        return super().__str__() + f", класс - ВНЕДОРОЖНИК, рама: {self.__frame}, привод: {self.__awd}, АБС: {self.__abs}."

    @property
    def frame(self):
        return self.__frame

    @frame.setter
    def frame(self, value):
        self.__frame = value

    @property
    def awd(self):
        return self.__awd

    @awd.setter
    def awd(self, value):
        self.__awd = value

    @property
    def abs(self):
        return self.__abs

    @abs.setter
    def abs(self, value):
        self.__abs = value


class Cargo(Car):
    __tonnage = 0
    __trailer = str()
    __sleeping_place = str()
    __seats = 0

    def __init__(self, price: int = 0, name: str = "", power: int = 0, color: str = "", tonnage: int = 0,
                 trailer: str = "", sleeping_place: str = "", seats: int = 0):
        super().__init__(price, name, power, color)
        self.__tonnage = tonnage
        self.__trailer = trailer
        self.__sleeping_place = sleeping_place
        self.__seats = seats

    def __del__(self):
        pass

    def __str__(self):
        return super().__str__() + f", класс - ГРУЗОВИК, тоннаж: {self.__tonnage} т, прицеп: {self.__trailer}, спальное место: {self.__sleeping_place}, сидений: {self.__seats}."

    @property
    def tonnage(self):
        return self.__tonnage

    @tonnage.setter
    def tonnage(self, value):
        if value < 0:
            raise ValueError("Тоннаж не может быть отрицательным.")
        self.__tonnage = value

    @property
    def trailer(self):
        return self.__trailer

    @trailer.setter
    def trailer(self, value):
        self.__trailer = value

    @property
    def sleeping_place(self):
        return self.__sleeping_place

    @sleeping_place.setter
    def sleeping_place(self, value):
        self.__sleeping_place = value

    @property
    def seats(self):
        return self.__seats

    @seats.setter
    def seats(self, value):
        if value < 0:
            raise ValueError("Кол-во сидений не может быть отрицательным.")
        self.__seats = value
