import time


class PrimeFinder:
    def __init__(self):
        self.primes = []

    def timer_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"Время выполнения: {end_time - start_time:.4f} секунд")
            return result
        return wrapper

    @timer_decorator
    def find_primes_in_range(self, start, end):
        self.primes = []
        for num in range(max(2, start), end + 1):
            is_prime = True
            for i in range(2, int(num**0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                self.primes.append(num)
        return self.primes

    def __del__(self):
        pass

    def __str__(self):
        return f"Найдено простых чисел: {len(self.primes)}"


if __name__ == "__main__":
    start_range = 10
    end_range = 1000
    prime_finder = PrimeFinder()
    primes_in_range = prime_finder.find_primes_in_range(start_range, end_range)
    print(f"Простые числа от {start_range} до {end_range}:", primes_in_range)
    print(prime_finder)
