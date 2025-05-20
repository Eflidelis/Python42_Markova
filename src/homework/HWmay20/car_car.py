class Car:
    def __init__(self, model: str = "Tesla", year: int = 2022, manufacturer: str = "Tesla",
                 engine_volume: float = 2.0, color: str = "Red", price: float = 50000):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def __del__(self):
        pass

    def input_data(self, model: str = None, year: int = None, manufacturer: str = None,
                   engine_volume: float = None, color: str = None, price: float = None):
        self.__model = model if model is not None else self.__model
        self.__year = year if year is not None and year > 1885 else self.__year
        self.__manufacturer = manufacturer if manufacturer is not None else self.__manufacturer
        self.__engine_volume = engine_volume if engine_volume is not None and engine_volume > 0 else self.__engine_volume
        self.__color = color if color is not None else self.__color
        self.__price = price if price is not None and price >= 0 else self.__price

    def get_data(self):
        return (f"Модель: {self.__model}\n"
                f"Год: {self.__year}\n"
                f"Производитель: {self.__manufacturer}\n"
                f"Объем двигателя: {self.__engine_volume}\n"
                f"Цвет: {self.__color}\n"
                f"Цена: {self.__price}")

    def __str__(self):
        return self.get_data()

    def __eq__(self, other):
        if isinstance(other, Car):
            return self.__model == other.__model and self.__manufacturer == other.__manufacturer
        return False

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_model: str):
        self.__model = new_model

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, new_year: int):
        if new_year > 1885:
            self.__year = new_year

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, new_manufacturer: str):
        self.__manufacturer = new_manufacturer

    @property
    def engine_volume(self):
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, new_volume: float):
        if new_volume > 0:
            self.__engine_volume = new_volume

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color: str):
        self.__color = new_color

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price >= 0:
            self.__price = new_price
