class Stadium:
    def __init__(self, name: str = "Camp Nou", opening_date: str = "1957-09-24",
                 country: str = "Spain", city: str = "Barcelona", capacity: int = 99354):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __del__(self):
        pass

    def input_data(self, name: str = None, opening_date: str = None, country: str = None,
                   city: str = None, capacity: int = None):
        self.__name = name if name else self.__name
        self.__opening_date = opening_date if opening_date else self.__opening_date
        self.__country = country if country else self.__country
        self.__city = city if city else self.__city
        self.__capacity = capacity if capacity is not None and capacity > 0 else self.__capacity

    def get_data(self):
        return (f"Стадион: {self.__name}\n"
                f"Дата открытия: {self.__opening_date}\n"
                f"Страна: {self.__country}\n"
                f"Город: {self.__city}\n"
                f"Вместимость: {self.__capacity}")

    def __str__(self):
        return self.get_data()

    def __eq__(self, other):
        if isinstance(other, Stadium):
            return self.__name == other.__name and self.__city == other.__city
        return False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, new_name: str):
        self.__name = new_name

    @property
    def opening_date(self):
        return self.__opening_date

    @opening_date.setter
    def opening_date(self, new_opening_date: str):
        self.__opening_date = new_opening_date

    @property
    def country(self):
        return self.__country

    @country.setter
    def country(self, new_country: str):
        self.__country = new_country

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, new_city: str):
        self.__city = new_city

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity: int):
        if new_capacity > 0:
            self.__capacity = new_capacity
