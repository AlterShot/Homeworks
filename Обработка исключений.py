try:
    num1 = int(input("Введите первое число: "))
    num2 = int(input("Введите второе число: "))
    result = num1 / num2
except ValueError:
    print("Одно из введенных чисел не является числом")
except ZeroDivisionError:
    print("На ноль делить нельзя!")
else:
    print(f"Результат: {result}")
finally:
    print("Программа закончила работу")
