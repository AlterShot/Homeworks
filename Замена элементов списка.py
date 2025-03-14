def swap():
    number_list = [1, 2, 3, 4, 5]
    print(number_list)
    last = number_list.pop(-1)
    first = number_list.pop(0)
    number_list.insert(0, last)
    number_list.append(first)
    return number_list


new_list = swap()
print(new_list)