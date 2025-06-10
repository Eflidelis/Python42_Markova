class BuildingComponent:
    __area = 0
    __el = 0
    __price = 1000

    def __init__(self, area: float = 0, el : int = 0, price : int = 1000):
        self.__area = area
        self.__el = el
        self.__price = price

    def __del__(self):
        pass

    def __str__(self):
        return f"Объект недвижимости общей площадью {self.__area} стоит {self.__price} рублей"

    @property
    def area(self):
        return self.__area

    @area.setter
    def area(self, value):
        self.__area = value

    @property
    def el(self):
        return self.__el

    @el.setter
    def el(self, value):
        self.__el = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = value



class Basement(BuildingComponent):
    __fund = str()
    __comm = str()


    def __init__(self, area: float = 0, el : int = 0, price : int = 1000, fund : str = "", comm : str = ""):
        super().__init__(area, el, price)
        self.__fund = fund
        self.__comm = comm

    def __del__(self):
        pass

    def basement_cost(self):
        total = self.__area * 1000 + self.__el * 100 + self.__price * 10
        return total

    @property
    def fund(self):
        return self.__fund

    @fund.setter
    def fund(self, value):
        self.__fund = value

    @property
    def comm(self):
        return self.__comm

    @comm.setter
    def comm(self, value):
        self.__comm = value


class Floor(BuildingComponent):
    __room = 0
    __wc = 0


    def __init__(self, area: float = 0, el : int = 0, price : int = 1000, room : int = 0, wc : int = 0):
        super().__init__(area, el, price)
        self.__room = room
        self.__wc = wc


    def __del__(self):
        pass


    def floor_cost(self):
        total = self.__area * 1000 + self.__el * 100 + self.__price * 10 + self.__room * 100 + self.__wc * 50
        return total

    @property
    def room(self):
        return self.__room

    @room.setter
    def room(self, value):
        self.__room = value

    @property
    def wc(self):
        return self.__wc

    @wc.setter
    def wc(self, value):
        self.__wc = value


class Roof(BuildingComponent):
    __type = str()
    __satellite = str()

    def __init__(self, area: float = 0, el : int = 0, price : int = 1000, type : str = "0", satellite : str = ""):
        super().__init__(area, el, price)
        self.__type = type
        self.__satellite = satellite

    def __del__(self):
        pass

    def roof_cost(self):
        total = self.__area * 1000 + self.__el * 100 + self.__price * 10
        return total

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    @property
    def satellite(self):
        return self.__satellite

    @satellite.setter
    def satellite(self, value):
        self.__satellite = value


class AddBuildings(BuildingComponent):
    __types = str()

    def __init__(self, area: float = 0, el : int = 0, price : int = 1000, types : str = ""):
        super().__init__(area, el, price)
        self.__types = types

    def __del__(self):
        pass

    def add_buildings_cost(self):
        total = self.__area * 1000 + self.__el * 100 + self.__price * 10
        return total

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        self.__types = value


class House():

    def __init__(self, basement : Basement, floor : Floor, roof : Roof, add_buildings : AddBuildings):
        self.__basement = basement
        self.__floor = floor
        self.__roof = roof
        self.__add_buildings = add_buildings


    def total_cost(self):
        total = (self.__basement.basement_cost()) + (self.__floor.floor_cost()) + (self.__roof.roof_cost()) + (self.__add_buildings.add_buildings_cost())
        return total



