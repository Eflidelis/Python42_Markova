class Book:
    def __init__(self, title: str = "Название", autor: str = "Автор", genre: str = "Жанр",
                 year: int = 1970, publisher: str = "Издание", price: float = 0.0):
        self.__title = title
        self.__year = year
        self.__publisher = publisher
        self.__genre = genre
        self.__autor = autor
        self.__price = price

    def __del__(self):
        pass

    def input_data(self, title: str = None, autor: str = None, genre: str = None,
                   year: int = None, publisher: str = None, price: float = None):
        self.__title = title if title is not None else self.__title
        self.__year = year if year is not None else self.__year
        self.__publisher = publisher if publisher is not None else self.__publisher
        self.__genre = genre if genre is not None else self.__genre
        self.__autor = autor if autor is not None else self.__autor
        self.__price = price if price is not None else self.__price

    def get_data(self):
        return (f"{self.__autor} - {self.__title}\n"
                f"Жанр: {self.__genre}\tГод: {self.__year}\n"
                f"Издание: {self.__publisher}\tЦена: {self.__price}")

    def __str__(self):
        return self.get_data()

    def __eq__(self, other):
        if isinstance(other, Book):
            return self.__title == other.__title and self.__autor == other.__autor
        return False

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor: str = None):
        if autor is not None:
            self.__autor = autor

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str = None):
        if title is not None:
            self.__title = title

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year: int = None):
        if year is not None:
            self.__year = year

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float = None):
        if price is not None:
            self.__price = price

    @property
    def genre(self):
        return self.__genre

    @genre.setter
    def genre(self, genre: str = None):
        if genre is not None:
            self.__genre = genre

    @property
    def publisher(self):
        return self.__publisher

    @publisher.setter
    def publisher(self, publisher: str = None):
        if publisher is not None:
            self.__publisher = publisher
