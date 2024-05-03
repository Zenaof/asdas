operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
    "//": lambda a, b: a // b,
}


def get_operation_input():
    while True:
        operation = input("Введите операцию (+, -, *, /, //): ")
        if operation in operations:
            return operation
        print("Неверная операция. Пожалуйста, введите одну из следующих операций: +, -, *, /, //")


def get_numbers_input():
    while True:
        try:
            a = float(input("Введите первое число: "))
            b = float(input("Введите второе число: "))
            return a, b
        except ValueError:
            print("Неверный ввод числа. Пожалуйста, введите число.")


def print_result(result):
    print(f"Результат: {result}")


def main():
    print("Добро пожаловать в калькулятор!")
    while True:
        operation = get_operation_input()
        a, b = get_numbers_input()
        result = operations[operation](a, b)
        print_result(result)

        choice = input("Хотите продолжить (y/n): ")
        if choice.lower() == "n":
            break

    print("Спасибо за использование калькулятора!")


if __name__ == "__main__":
    main()