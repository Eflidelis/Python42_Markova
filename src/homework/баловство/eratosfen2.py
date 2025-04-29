def sieve_of_eratosthenes(limit):
    if limit < 2:
        return []

    is_prime = [True] * ((limit // 2) + 1)  # Для нечетных чисел от 3 до limit
    is_prime[0] = False

    for num in range(3, int(limit ** 0.5) + 1, 2):
        if is_prime[num // 2]:  # Проверяем только нечетные
            for multiple in range(num * num, limit + 1, num * 2):
                is_prime[multiple // 2] = False  # помечаем как составное

    primes = [2] + [num for num in range(3, limit + 1, 2) if is_prime[num // 2]]

    return primes

# 100 лямов за 10 секунд :)
primes = sieve_of_eratosthenes(100000000)
print("Простые числа в указанном диапазоне:", primes)
