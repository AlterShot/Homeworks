def cycle(list_one, list_two):
    new_list = []

    max_len = max(len(list_one), len(list_two))

    for number in range(max_len):
        number_one = list_one[number] if number < len(list_one) else 0
        number_two = list_two[number] if number < len(list_two) else 0
        new_list.append(number_one + number_two)
    return new_list


def cycle_two(list_one, list_two):
    for number in range(min(len(list_one), len(list_two))):
        list_one[number] += list_two[number]
    if len(list_two) > len(list_one):
        list_one.extend(list_two[len(list_one):])
    return list_one


result = cycle([1, 2, 3, 4, 5, 6, 7], [7, 8, 9, 0, 10, 11])
result_two = cycle_two([1, 2, 3, 4, 5, 6, 7], [7, 8, 9, 0, 10])
print(result, result_two)
