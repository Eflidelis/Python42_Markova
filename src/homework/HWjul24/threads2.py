import threading
import random
import os


def fill_file(file_path, size):
    with open(file_path, 'w') as f:
        for _ in range(size):
            num = random.randint(1, 100)
            f.write(f"{num}\n")
            print(f"Добавлено число: {num}")


def find_primes(file_path, output_file):
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    primes = [num for num in numbers if all(num % i != 0 for i in range(2, int(num**0.5) + 1) if num > 1)]
    with open(output_file, 'w') as f:
        for prime in primes:
            f.write(f"{prime}\n")
    print(f"Найдено простых чисел: {len(primes)}")


def calculate_factorials(file_path, output_file):
    with open(file_path, 'r') as f:
        numbers = [int(line.strip()) for line in f]
    factorials = [str(factorial(num)) for num in numbers]
    with open(output_file, 'w') as f:
        for fact in factorials:
            f.write(f"{fact}\n")
    print(f"Факториалы вычислены для {len(numbers)} чисел")


def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def main(file_path):
    fill_thread = threading.Thread(target=fill_file, args=(file_path, 10))
    primes_thread = threading.Thread(target=find_primes, args=(file_path, 'primes.txt'))
    factorials_thread = threading.Thread(target=calculate_factorials, args=(file_path, 'factorials.txt'))

    fill_thread.start()
    fill_thread.join()

    primes_thread.start()
    factorials_thread.start()

    primes_thread.join()
    factorials_thread.join()


if __name__ == "__main__":
    file_path = input("Введите путь к файлу: ")
    main(file_path)
