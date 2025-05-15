class Car:
    def __init__(self, model="Tesla", year=2022, manufacturer="Tesla", engine_volume=2.0, color="Red", price=50000):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price

    def input_data(self):
        self.__model = input("Enter car model: ")
        self.__year = input("Enter year of manufacture: ")
        self.__manufacturer = input("Enter manufacturer: ")
        self.__engine_volume = input("Enter engine volume: ")
        self.__color = input("Enter car color: ")
        self.__price = float(input("Enter price: "))

    def output_data(self):
        print(f"Model: {self.__model}, Year: {self.__year}, Manufacturer: {self.__manufacturer}, "
              f"Engine Volume: {self.__engine_volume}, Color: {self.__color}, Price: {self.__price}")

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


