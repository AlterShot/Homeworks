def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return
    print("Список книг: ")
    for book in library:
        print(book)


def add_book(library, title, author, year):
    if not title or not author or not year:
        print("Название, автор и год должны быть указаны")
        return

    if title in library:
        print(f"\"{title}\" уже существует. Желаете обновить? (да/нет) ")
        option = input().lower()
        if option == "да":
            library[title]["author"] = author
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
        status = "Книга доступна" if book["in_stock"] else "Книга выдана" if book["in_stock"] is False \
            else "Книга в библиотеке, но ее статус не определен"
        print(f"Информация о книге \"{title}\":"
              f"\nАвтор: {book['author']}"
              f"\nГод издания: {book['year']}"
              f"\n{status}")

    else:
        print("Книга не найдена. Проверьте корректность ввода")


def get_out():
    return False


def play_with_library():
    main_menu = {
        "1": lambda: book_list_view(library),
        "2": lambda: add_book(library, (input("Введите название книги: ")),
                              (input("Укажите автора: ")),
                              int(input("Год написания: "))),
        "3": lambda: remove_book(library, input("Какую книгу удалить? ")),
        "4": lambda: issue_book(library, input("Какую книгу выдать? ")),
        "5": lambda: return_book(library, input("Какую книгу вернуть? ")),
        "6": lambda: find_book(input("Какая книга интересует? "), library),
        "7": get_out
    }

    flag = True
    while flag:
        option = input("1. Список книг\n2. Добавить/Обновить книгу\n3. Удалить книгу"
                       "\n4. Взять книгу\n5. Вернуть книгу\n6. Информация о книге\n7. Выход\nВаш выбор: ")
        if option == "7":
            flag = get_out()
        elif option in main_menu:
            main_menu[option]()
        else:
            print("Такого в меню нет.")


library = {
    "Мертвые души": {"author": "Гоголь", "year": 1850, "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": 2024, "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": 1320, "in_stock": True},
    "1984": {"author": "Хаксли", "year": 1960, "in_stock": False}
}

play_with_library()
