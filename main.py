try:
    print("Операция сложения")
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    print(number_one + number_two)
except ValueError:
    print("Введенные данные не являются числом")

try:
    print("Операция вычитания")
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    print(number_one - number_two)
except ValueError:
    print("Введенные данные не являются числом")

try:
    print("Операция умножения")
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    print(number_one * number_two)
except ValueError:
    print("Введенные данные не являются числом")

try:
    print("Операция деления")
    number_one = int(input("Введите первое число: "))
    number_two = int(input("Введите второе число: "))
    print(number_one / number_two)
except ValueError:
    print("Введенные данные не являются числом")
except ZeroDivisionError:
    print("Нельзя делить не ноль")
finally:
    print("Программа завершила работу")
