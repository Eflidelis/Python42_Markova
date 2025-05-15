class Book:
    def __init__(self, title: str = "1984", year: int = 1949, publisher: str = "Secker & Warburg", genre: str = "Dystopian", author: str = "George Orwell", price: float = 15.99):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__author = author
        self.__price = price

    def __del__(self):
        pass

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, new_title: str):
        self.__title = new_title

    @property
    def year(self) -> int:
        return self.__year

    @property
    def publisher(self) -> str:
        return self.__publisher

    @property
    def genre(self) -> str:
        return self.__genre

    @property
    def author(self) -> str:
        return self.__author

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price >= 0:
            self.__price = new_price

    def say_info(self) -> str:
        return f"Book Title: {self.__title}, Year: {self.__year}, Publisher: {self.__publisher}, Genre: {self.__genre}, Author: {self.__author}, Price: {self.__price}"
