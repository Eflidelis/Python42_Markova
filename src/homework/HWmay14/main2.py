from o_car import Car
from o_book import Book
from o_stadium import Stadium

if __name__ == "__main2__":
    car = Car()
    book = Book()
    stadium = Stadium()

    print(car.say_info())
    print(book.say_info())
    print(stadium.say_info())

    car.price = 60000
    book.title = "Brave New World"
    stadium.capacity = 90000

    print("\nUpdated Information:")
    print(car.say_info())
    print(book.say_info())
    print(stadium.say_info())
