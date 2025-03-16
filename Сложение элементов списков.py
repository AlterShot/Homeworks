def cycle():
    list_one = [1, 2, 3, 4, 5]
    list_two = [5, 4, 3, 2, 1, 6, 7]
    new_list = []

    if len(list_one) > len(list_two):
        while len(list_two) < len(list_one):
            list_two.append(0)
    elif len(list_two) > len(list_one):
        while len(list_one) < len(list_two):
            list_one.append(0)

    for number in range(len(list_one)):
        result_one = list_one[number] + list_two[number]
        new_list.append(result_one)
    return new_list


result = cycle()
print(result)
