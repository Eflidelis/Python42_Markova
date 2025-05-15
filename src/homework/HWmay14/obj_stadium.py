class Stadium:
    def __init__(self, name="Camp Nou", opening_date="1957-09-24", country="Spain", city="Barcelona", capacity=99354):
        self.__name = name
        self.__opening_date = opening_date
        self.__country = country
        self.__city = city
        self.__capacity = capacity

    def input_data(self):
        self.__name = input("Enter stadium name: ")
        self.__opening_date = input("Enter opening date: ")
        self.__country = input("Enter country: ")
        self.__city = input("Enter city: ")
        self.__capacity = int(input("Enter capacity: "))

    def output_data(self):
        print(f"Stadium Name: {self.__name}, Opening Date: {self.__opening_date}, "
              f"Country: {self.__country}, City: {self.__city}, Capacity: {self.__capacity}")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_capacity(self):
        return self.__capacity

    def set_capacity(self, capacity):
        self.__capacity = capacity


