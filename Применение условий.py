def all_even_sum():
    hundred = []
    for number in range(0, 101):
        if number % 2 == 0:
            hundred.append(number)
    result = sum(hundred)
    return result


def squares_count():
    squares = [number ** 2 for number in range(0, 11) if number % 2 != 0]
    return squares


def user_printing():
    number_count = 0
    while True:
        user_input = int(input("Введите число. Выход - отрицательное число: "))
        if user_input < 0:
            break
        number_count += 1
    return number_count


def show():
    even_sum = all_even_sum()
    all_squares = squares_count()
    quantity = user_printing()
    print(f"Сумма четных чисел: {even_sum}")
    print(f"Квадраты нечетных чисел: {all_squares}")
    print(f"Количество чисел: {quantity}")


show()
