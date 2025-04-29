def filter_and_subtract():
    upper_limit = 10000000
    lst1 = set(range(2, upper_limit + 1))
    lst2 = set()

    # Исключаем четные числа, кроме 2
    lst1 = {num for num in lst1 if num % 2 != 0 or num == 2}

    # кратность на все нечетные числа от 3 до корня из upper_limit
    for i in range(3, int(upper_limit**0.5) + 1, 2):
        if i in lst1:
            for j in range(2, upper_limit // i + 1):
                lst2.add(i * j)

    # Удаляем кратные из lst1 10 ЛЯМОВ ЗА 6 СЕКУНД, 100 лямов не берет уже
    result = lst1 - lst2

    print("Простые числа в указанном диапазоне:", sorted(result))

filter_and_subtract()
