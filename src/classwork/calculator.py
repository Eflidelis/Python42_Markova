def calc():
    '''
    функция калькулятора
    :return: результат вычислений
    '''

    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    sign = input("Введите знак операции: ")
    result = 0

    if sign == "+":
        result = num1 + num2
        print(result)
    elif sign == "-":
        result = num1 - num2
        print(result)
    elif sign == "*":
        result = num1 * num2
        print(result)
    elif sign == "/":
        result = num1 / num2
        print(result)
    elif sign == "^":
        result = num1 ** num2
        print(result)
    else:
        print("Некорректный знак операции")

    return result

calc()
