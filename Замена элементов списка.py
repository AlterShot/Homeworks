def define_list():
    number_list = [1, 2, 3, 4, 5]
    return number_list


def swap(number_list):
    last = number_list.pop(-1)
    first = number_list.pop(0)
    number_list.insert(0, last)
    number_list.append(first)
    return number_list


def printing():
    new_list = swap(define_list())
    print(new_list)


printing()