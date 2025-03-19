def counting_unique(list):
    while True:
        user_entering = input(f"Введите число (для завершения введите \"q\"): ")
        if user_entering == "q":
            break
        try:
            user_entering = int(user_entering)
            this_list.append(user_entering)
        except ValueError:
            print("Нужно ввести число")
    return this_list


this_list = []

u_list = set(counting_unique(this_list))

print(f"Уникальных значений: {len(u_list)}")
