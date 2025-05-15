class Book:
    def __init__(self, title="1984", year=1949, publisher="Secker & Warburg", genre="Dystopian", author="George Orwell", price=15.99):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def input_data(self):
        self.__title = input("Enter book title: ")
        self.__year = input("Enter year of publication: ")
        self.__publisher = input("Enter publisher: ")
        self.__genre = input("Enter genre: ")
        self.__author = input("Enter author: ")
        self.__price = float(input("Enter price: "))

    def output_data(self):
        print(f"Title: {self.__title}, Year: {self.__year}, Publisher: {self.__publisher}, "
              f"Genre: {self.__genre}, Author: {self.__author}, Price: {self.__price}")

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


