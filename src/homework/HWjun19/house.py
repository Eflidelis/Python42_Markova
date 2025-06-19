class BuildingComponent:
    __area = 0
    __el = 0
    __price = 1000

    def __init__(self, area: float = 0, el: int = 0, price: int = 1000):
        self.__area = area
        self.__el = el
        self.__price = price

    def __str__(self):
        return f"Объект недвижимости общей площадью {self.__area} стоит {self.__price} рублей"

    @property
    def area(self):
        return self.__area

    @property
    def el(self):
        return self.__el

    @property
    def price(self):
        return self.__price


class Basement(BuildingComponent):
    __fund = str()
    __comm = str()

    fund_coefficients = {
        "ленточный": 1.2,
        "плита": 1.5,
        "сваи": 1.8
    }

    comm_coefficients = {
        "электричество": 1.1,
        "вода": 1.2,
        "газ": 1.3
    }

    def __init__(self, area: float = 0, el: int = 0, price: int = 1000, fund: str = "", comm: str = ""):
        super().__init__(area, el, price)
        self.__fund = fund
        self.__comm = comm

    def basement_cost(self):
        fund_coeff = self.fund_coefficients.get(self.__fund, 1)
        comm_coeff = self.comm_coefficients.get(self.__comm, 1)
        total = (self.area * 1000 * fund_coeff +
                 self.el * 100 * comm_coeff +
                 self.price * 10)
        return total


class Floor(BuildingComponent):
    __room = 0
    __wc = 0

    def __init__(self, area: float = 0, el: int = 0, price: int = 1000, room: int = 0, wc: int = 0):
        super().__init__(area, el, price)
        self.__room = room
        self.__wc = wc

    def floor_cost(self):
        total = (self.area * 1000 +
                 self.el * 100 +
                 self.price * 10 +
                 self.__room * 100 +
                 self.__wc * 50)
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

    roof_coefficients = {
        "черепица": 1.2,
        "плоская": 1.5,
        "металлочерепица": 1.8
    }

    satellite_coefficients = {
        "спутник": 1.2,
        "кабель": 1.1,
        "интернет": 1.3
    }

    def __init__(self, area: float = 0, el: int = 0, price: int = 1000, type: str = "0", satellite: str = ""):
        super().__init__(area, el, price)
        self.__type = type
        self.__satellite = satellite

    def roof_cost(self):
        roof_coeff = self.roof_coefficients.get(self.__type, 1)
        satellite_coeff = self.satellite_coefficients.get(self.__satellite, 1)
        total = (self.area * 1000 * roof_coeff +
                 self.el * 100 +
                 self.price * 10 * satellite_coeff)
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

    add_buildings_coefficients = {
        "курятник": 1.1,
        "гараж": 1.5,
        "беседка": 1.2
    }

    def __init__(self, area: float = 0, el: int = 0, price: int = 1000, types: str = ""):
        super().__init__(area, el, price)
        self.__types = types

    def add_buildings_cost(self):
        coeff = self.add_buildings_coefficients.get(self.__types, 1)
        total = (self.area * 1000 * coeff +
                 self.el * 100 +
                 self.price * 10)
        return total

    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, value):
        self.__types = value


class House:
    def __init__(self, basement: Basement, floor: Floor, roof: Roof, add_buildings: AddBuildings):
        self.__basement = basement
        self.__floor = floor
        self.__roof = roof
        self.__add_buildings = add_buildings

    def total_cost(self):
        total = (self.__basement.basement_cost() +
                 self.__floor.floor_cost() +
                 self.__roof.roof_cost() +
                 self.__add_buildings.add_buildings_cost())
        return total
