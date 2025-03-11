def max_number(a, b):

    if a >= b:
        return a
    else:
        return b

a = int(input("Enter first number to compare: "))
b = int(input("Enter second number to compare: "))
max_number(a, b)

def emtpy_function():
    pass

def even_numbers(n):
    for i in range(n + 1):
        yield i

for n in even_numbers(3):
    if n % 2 == 0:
        print(n)

def test_max_number():

    assert max_number(10, 20) == 20, "Error, should\'ve been 20"
    assert max_number(45, 5) == 45, "Error, should\'ve been 45"
    assert max_number(51, 51) == 51, "Error, should\'ve been 51"

test_max_number()


