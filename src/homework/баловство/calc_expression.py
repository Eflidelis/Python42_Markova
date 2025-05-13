def get_sign_precedence(sign):
    if sign in ('+', '-'):
        return 1
    if sign in ('*', '/'):
        return 2
    if sign == '^':
        return 3
    return 0

def perform_operation(num1, num2, sign):
    if sign == '+':
        return num1 + num2
    if sign == '-':
        return num1 - num2
    if sign == '*':
        return num1 * num2
    if sign == '/':
        return num1 / num2
    if sign == '^':
        return num1 ** num2

def evaluate_math_expression(expr):
    num_stack = []
    sign_stack = []
    idx = 0

    while idx < len(expr):
        if expr[idx] == ' ':
            idx += 1
            continue

        if expr[idx].isdigit():
            number = 0
            while (idx < len(expr) and expr[idx].isdigit()):
                number = (number * 10) + int(expr[idx])
                idx += 1
            num_stack.append(number)
            idx -= 1
        elif expr[idx] == '(':
            sign_stack.append(expr[idx])
        elif expr[idx] == ')':
            while sign_stack and sign_stack[-1] != '(':
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                sign = sign_stack.pop()
                num_stack.append(perform_operation(num1, num2, sign))
            sign_stack.pop()
        else:
            while (sign_stack and get_sign_precedence(sign_stack[-1]) >= get_sign_precedence(expr[idx])):
                num2 = num_stack.pop()
                num1 = num_stack.pop()
                sign = sign_stack.pop()
                num_stack.append(perform_operation(num1, num2, sign))
            sign_stack.append(expr[idx])
        idx += 1

    while sign_stack:
        num2 = num_stack.pop()
        num1 = num_stack.pop()
        sign = sign_stack.pop()
        num_stack.append(perform_operation(num1, num2, sign))

    return num_stack[0]

def main():
    user_expr = input("Введите математическое выражение: ")
    result = evaluate_math_expression(user_expr)
    print(f"Результат: {result}")

if __name__ == "__main__":
    main()
