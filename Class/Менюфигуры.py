from Фигура import Rectangle, Circle


def get_out():
    return False


def play_with_shapes():
    main_menu = {
        "1": lambda: print(f"Площадь прямоугольника: "
                           f"{Rectangle(float(input("Укажите ширину прямоугольника: ")),
                                        float(input("Укажите длину прямоугольника: "))).area():.1f}"),
        "2": lambda: print(f"Площадь круга: {Circle(float(input("Укажите радиус круга: "))).area():.1f}")
    }

    flag = True
    while flag:
        option = input("1. Рассчитать площадь прямоугольника\n2. Рассчитать площадь круга\n"
                       "3. Выход\nВаш выбор: ")
        if option == "3":
            flag = get_out()
        elif option in main_menu:
            main_menu[option]()
        else:
            print("Такого в меню нет.")


play_with_shapes()
