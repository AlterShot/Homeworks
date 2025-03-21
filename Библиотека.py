def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return
    print("Список книг: ")
    for book in library:
        print(book)


def add_book(library, title, author, year):
    if title in library:
        print(f"\"{title}\" уже существует. Желаете обновить? (да/нет) ")
        option = input().lower()
        if option == "да":
            if author:
                library[title]["author"] = author
            if year:
                library[title]["year"] = year
            library[title]["in_stock"] = None
            print(f"Информация о книге \"{title}\" успешно обновлена")
        elif option == "нет":
            print("Отмена.")
        else:
            print("Введена некорректная команда")
    else:
        library[title] = {"author": author, "year": year, "in_stock": None}
        print(f"Книга \"{title}\" добавлена")


def remove_book(title, library):
    if title in library:
        del library[title]
        print(f"Книга \"{title}\" удалена")
    else:
        print(f"Книги с названием \"{title}\" не существует")


def issue_book(title, library):
    if title in library:
        if library[title]["in_stock"]:
            library[title]["in_stock"] = False
            print(f"Книгу \"{title}\" взяли")
        else:
            print(f"Книга \"{title}\" недоступна")
    else:
        print("Такой книги нет")


def return_book(title, library):
    if title in library:
        if not library[title]["in_stock"]:
            library[title]["in_stock"] = True
            print(f"Книгу \"{title}\" вернули")
        else:
            print(f"Книга \"{title}\" доступна")
    else:
        print("Такой книги нет")


def find_book(title, library):
    if title in library:
        book = library[title]
        print(f"Информация о книге \"{title}\":"
              f"\nАвтор: {book["author"]}"
              f"\nГод издания: {book["year"]}"
              f"\n{"Книга доступна" if book["in_stock"] else "Книга выдана" if not book["in_stock"]
              else "Книга в библиотеке, но ее статус не определен"}")

    else:
        print("Книга не найдена. Проверьте корректность ввода")


def get_out():
    print("Пока!")
    return


def play_with_library():
    main_menu = {
        "1": book_list_view,
        "2": lambda: add_book(library, str(input("Введите название книги: ")),
                              str(input("Укажите автора: ")),
                              int(input("Год написания: "))),
        "3": remove_book,
        "4": issue_book,
        "5": return_book,
        "6": find_book,
        "7": get_out
    }

    while True:
        option = input("1. Список книг 2. Добавить/Обновить книгу 3. Удалить книгу"
                       " 4. Взять книгу 5. Вернуть книгу 6. Информация о книге 7. Выход ")
        if option == "7":
            main_menu[option]()
            break
        elif option == "2":
            main_menu[option]()
        elif option == "1":
            main_menu[option](library)
        elif option in main_menu:
            title = input("Введите название книги: ")
            main_menu[option](title, library)
        else:
            print("Такого в меню нет.")


library = {
    "Мертвые души": {"author": "Гоголь", "year": 1850, "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": 2024, "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": 1320, "in_stock": True},
    "1984": {"author": "Хаксли", "year": 1960, "in_stock": False}
}

play_with_library()
