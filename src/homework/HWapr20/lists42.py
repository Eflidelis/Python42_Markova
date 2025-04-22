def extract_parts(expression):
    '''
    Извлекает числа и знак из выражения

    :param expression: мат.выражение в формате "число знак число"
    :return: кортеж, содержащий список чисел (в формате int) и строку со знаком
    '''
    parts = []
    numbers = []
    operator = ''

    for char in expression:
        if char.isdigit() or char in '+-*/':
            parts.append(char)

    current_number = ''
    for part in parts:
        if part.isdigit():
            current_number += part
        else:
            numbers.append(int(current_number))
            operator = part
            current_number = ''

    if current_number:
        numbers.append(int(current_number))

    return numbers, operator


def main():
    '''
    Основная функция программы, которая запрашивает у пользователя
    мат. выражение, извлекает числа и знак,
    вычисляет результат и выводит его на экран

    :return: none
    '''
    expression = input("Введите выражение (например, 23+12): ")

    numbers, operator = extract_parts(expression)

    if operator == '+':
        result = numbers[0] + numbers[1]
    elif operator == '-':
        result = numbers[0] - numbers[1]
    elif operator == '*':
        result = numbers[0] * numbers[1]
    elif operator == '/':
        result = numbers[0] / numbers[1] if numbers[1] != 0 else "Ошибка: деление на ноль"
    else:
        result = "Ошибка: неверный знак действия"

    print("Результат:", result)


if __name__ == "__main__":
    main()


