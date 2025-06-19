import json

class MusicAlbumManager:
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

    def add_band(self, band, album):
        if band in self.data:
            self.data[band].append(album)
        else:
            self.data[band] = [album]
        self.save_data()

    def remove_band(self, band):
        if band in self.data:
            del self.data[band]
            self.save_data()

    def find_albums(self, band):
        return self.data.get(band, "Группа не найдена")

    def edit_album(self, band, old_album, new_album):
        if band in self.data:
            if old_album in self.data[band]:
                index = self.data[band].index(old_album)
                self.data[band][index] = new_album
                self.save_data()


if __name__ == "__main__":
    manager = MusicAlbumManager("albums.json")

    manager.add_band("Queen", "Innuendo")

    print(manager.find_albums("Queen"))

    manager.edit_album("The Beatles", "Abbey Road", "Abbey Road Remastered")

    manager.remove_band("The Beatles")

    print(manager.data)
