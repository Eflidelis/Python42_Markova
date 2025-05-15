class Car:
    def __init__(self, model: str = "Tesla", year: int = 2022, manufacturer: str = "Tesla", engine_volume: float = 2.0, color: str = "Red", price: float = 50000):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def __del__(self):
        pass

    @property
    def model(self) -> str:
        return self.__model

    @model.setter
    def model(self, new_model: str):
        self.__model = new_model

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, new_year: int):
        if new_year > 1885:  # Год, когда была изобретена первая машина
            self.__year = new_year

    @property
    def manufacturer(self) -> str:
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, new_manufacturer: str):
        self.__manufacturer = new_manufacturer

    @property
    def engine_volume(self) -> float:
        return self.__engine_volume

    @engine_volume.setter
    def engine_volume(self, new_volume: float):
        if new_volume > 0:
            self.__engine_volume = new_volume

    @property
    def color(self) -> str:
        return self.__color

    @color.setter
    def color(self, new_color: str):
        self.__color = new_color

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price >= 0:
            self.__price = new_price

    def say_info(self) -> str:
        return f"Car Model: {self.__model}, Year: {self.__year}, Manufacturer: {self.__manufacturer}, Engine Volume: {self.__engine_volume}, Color: {self.__color}, Price: {self.__price}"
