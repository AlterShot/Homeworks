try:
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    operation = input(str("Желаемая математическая операция (+, -, *, /): "))
    if operation == "+":
        result = number_one + number_two
        print("Результат сложения: ", result)
    elif operation == "-":
        result = number_one - number_two
        print("Результат вычитания: ", result)
    elif operation == "*":
        result = number_one * number_two
        print("Результат умножения: ", result)
    elif operation == "/":
        result = number_one / number_two
        print("Результат деления: ", result)
    else:
        print("Неизвестная операция")
except ValueError:
    print("Введенные данные не являются числом")
except ZeroDivisionError:
    print("Нельзя делить не ноль")
finally:
    print("Программа завершила работу")
