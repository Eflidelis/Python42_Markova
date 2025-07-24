import threading
import random
import time


def fill_list(size):
    numbers = []
    for _ in range(size):
        num = random.randint(1, 100)
        numbers.append(num)
        print(f"Добавлено число: {num}")
        time.sleep(0.1)
    return numbers


def calculate_sum(numbers):
    total = sum(numbers)
    print(f"Сумма элементов списка: {total}")


def calculate_average(numbers):
    average = sum(numbers) / len(numbers) if numbers else 0
    print(f"Среднее значение элементов списка: {average}")


def main(size):
    numbers = fill_list(size)
    thread_sum = threading.Thread(target=calculate_sum, args=(numbers,))
    thread_average = threading.Thread(target=calculate_average, args=(numbers,))
    thread_sum.start()
    thread_average.start()
    thread_sum.join()
    thread_average.join()
    print(f"Заполненный список: {numbers}")


if __name__ == "__main__":
    main(10)
