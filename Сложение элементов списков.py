def cycle(list_one, list_two):
    long_one, long_two = len(list_one), len(list_two)
    for number in range(min(long_one, long_two)):
        list_one[number] += list_two[number]
    if long_two > long_one:
        list_one.extend(list_two[len(list_one):])
    return list_one


result = cycle([1, 2, 3, 4, 5, 6, 7], [7, 8, 9, 0, 10])
print(result)
