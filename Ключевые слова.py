def max_number(a, b):
    if a > b:
        print(f"Max value is {a}")
        return a
    elif a == b:
        print(f"These numbers are similar: {a}")
        return a
    else:
        print(f"Max value is {b}")
        return b

def emtpy_function():
    pass

def even_numbers(n):
    for i in range(n + 1):
        yield i

for n in even_numbers(25):
    if n % 2 == 0:
        print(n)

max_number(6, 6), max_number(1, 5), max_number(24, 7)

def test_max_number():
    assert max_number(10, 20) == 20
    assert max_number(45, 5) == 45
    assert max_number(51, 51) == 51

test_max_number()
print("Tests are made")

