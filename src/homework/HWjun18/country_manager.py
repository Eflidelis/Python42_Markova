import json

class CountryCapitalManager:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            print("Ошибка чтения файла .json")
            return {}

    def save_data(self):
        with open(self.filename, "w", encoding="utf-8") as file:
            json.dump(self.data, file, ensure_ascii=False, indent=4)

    def add_country(self, country, capital):
        self.data[country] = capital
        self.save_data()

    def remove_country(self, country):
        if country in self.data:
            del self.data[country]
            self.save_data()

    def find_capital(self, country):
        return self.data.get(country, "Страна не найдена")

    def edit_country(self, country, new_capital):
        if country in self.data:
            self.data[country] = new_capital
            self.save_data()


if __name__ == "__main__":
    manager = CountryCapitalManager("countries.json")

    manager.add_country("Италия", "Рим")

    print(manager.find_capital("Россия"))

    manager.edit_country("США", "Нью-Йорк")

    manager.remove_country("Франция")

    print(manager.data)
