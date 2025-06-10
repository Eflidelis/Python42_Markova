from building import Basement, Floor, Roof, AddBuildings, House

def main():

    basement = Basement(area=100, el=220, price=1000, fund="ленточный", comm="электричество")
    floor = Floor(area=200, el=220, price=2000, room=5, wc=2)
    roof = Roof(area=50, el=220, price=500, type="черепица", satellite="НТВ")
    add_buildings = AddBuildings(area=20, el=380, price=200, types="курятник")
    house = House()

    basement.basement_cost()
    floor.floor_cost()
    roof.roof_cost()
    add_buildings.add_buildings_cost()
    total_cost = house.total_cost()

    print(total_cost)

