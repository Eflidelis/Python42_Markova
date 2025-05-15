class Book:
    __title = str()
    __year = 1970
    __genre = str()
    __author = str()

    def __init__(self, title : str = "Название", author: str = "Автор", genre : str = "Жанр", year : int = 1970):
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__author = author

    def __del__(self):
        pass

    def input_data(self, title : str = "Название", author: str = "Автор", genre : str = "Жанр", year : int = 1970):
        self.__title = title
        self.__year = year
        self.__genre = genre
        self.__author = author

