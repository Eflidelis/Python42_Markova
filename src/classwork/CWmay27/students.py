class Person():
    __name = str()
    __age =  0

    def __init__(self, name : str = "", age : int = 0):
        self.__name = name
        self.__age = age

    def __del__(self):
        pass

    def str(self):
        return f"Имя: {self.__name}\nВозраст: {self.__age}"


class Lector(Person):
    __cathedra = str()

    def __init__(self, name : str = "", age : int = 0, cathedra : str = ""):
        super().__init__(name, age)
        self.__cathedra = cathedra

    def __del__(self):
        pass

    def func_lector(self):
        return f"Я преподаю {self.__cathedra}"


class Admin(Person):
    __cab = str()
    def __init__(self, name : str = "", age : int = 0, cab : str = ""):
        super().__init__(name, age)
        self.__cab = cab

    def __del__(self):
        pass

    def func_admin(self):
        return f"Моя должность - {self.__cab}"


pers = Person()
lector = Lector("Бронислав", 42, "ракетостроение")
admin = Admin("Валентина", 50, "библиотекарь")

