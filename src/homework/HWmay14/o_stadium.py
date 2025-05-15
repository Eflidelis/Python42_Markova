class Stadium:
    def __init__(self, name: str = "Camp Nou", opening_date: str = "1957-09-24", country: str = "Spain", city: str = "Barcelona", capacity: int = 99354):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def __del__(self):
        pass

    @property
    def name(self) -> str:
        return self.__name

    @property
    def opening_date(self) -> str:
        return self.__opening_date

    @property
    def country(self) -> str:
        return self.__country

    @property
    def city(self) -> str:
        return self.__city

    @property
    def capacity(self) -> int:
        return self.__capacity

    @capacity.setter
    def capacity(self, new_capacity: int):
        if new_capacity > 0:
            self.__capacity = new_capacity

    def say_info(self) -> str:
        return f"Stadium Name: {self.__name}, Opening Date: {self.__opening_date}, Country: {self.__country}, City: {self.__city}, Capacity: {self.__capacity}"
