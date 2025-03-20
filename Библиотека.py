def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return
    print("Список книг: ")
    for book in library:
        print(book)


def add_book(library, title, author, year):
    library[title] = {"author": author, "year": year, "in_stock": None}
    print(f"Книга \"{title}\" добавлена")


def update_book(library):
    title = input("Какую книгу хотите обновить? ")
    if title in library:
        new_author = input("Укажите нового автора: ")
        new_year = int(input("Новый год написания: "))
        library[title]["author"] = new_author
        try:
            library[title]["year"] = new_year
        except ValueError:
            print("Год введен некорректно.")
        library[title]["in_stock"] = None
        print(f"Информация о книге \"{title}\" успешно обновлена")
    else:
        print(f"Книга \"{title}\" не найдена")


def get_out():
    print("Пока!")
    return


def play_with_library(library):
    main_menu = {
        "1": book_list_view,
        "2": add_book,
        "3": update_book,
        "8": get_out
    }

    while True:
        option = input("1. Список книг 2. Добавить книгу 3. Обновить книгу 8. Выход ")
        if option == "8":
            main_menu[option]()
            break
        elif option == "2":
            title = str(input("Введите название книги: "))
            author = str(input("Укажите автора: "))
            year = int(input("Год написания: "))
            main_menu[option](library, title, author, year)
        elif option in main_menu:
            main_menu[option](library)
        else:
            print("Такого в меню нет.")


library = {
    "Мертвые души": {"author": "Гоголь", "year": "1850", "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": "2024", "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": "1320", "in_stock": True},
    "1984": {"author": "Хаксли", "year": "1960", "in_stock": False}
}

play_with_library(library)
