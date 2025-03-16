def cycle(list_one, list_two):
    new_list = []

    if len(list_one) > len(list_two):
        max_len = len(list_one)
    else:
        max_len = len(list_two)

    for number in range(max_len):
        result_pair_sum = list_one[number] + list_two[number]
        new_list.append(result_pair_sum)

    return new_list


result = cycle([1, 2, 3, 4, 5, 6], [7, 8, 9, 0, 10, 11])
print(result)
