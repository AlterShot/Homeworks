def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return
    print("Список книг: ")
    for book in library:
        print(book)


def add_book(library, title, author, year):
    library["title"] = {"author": author, "year": year, "in_stock": None}
    print(f"Книга \"{title}\" добавлена")
    book_list_view(library)


def update_book(library, title):
    print(f"\"{title}\" уже существует. Желаете обновить? (да/нет) ")
    option = input().lower()
    if option == "да":
        author = input("Укажите нового автора: ")
        year = int(input("Новый год написания: "))
        print(f"Информация о книге \"{title}\" успешно обновлена")
        book_list_view(library)
    elif option == "нет":
        print("Всего доброго!")
    else:
        print("Введена некорректная команда")


def play_with_library():
    option = input("1. Список книг 2. Добавить книгу ")
    try:
        if option == "1":
            book_list_view(library)
        elif option == "2":
            title = input("Введите название книги: ")
            if title in library:
                update_book(library, title)
            else:
                author = input("Укажите автора: ")
                year = int(input("Год написания: "))
                add_book(library, title, author, year)
    except ValueError:
        print("Год введен некорректно.")


library = {
    "Мертвые души": {"author": "Гоголь", "year": "1850", "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": "2024", "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": "1320", "in_stock": True},
    "1984": {"author": "Хаксли", "year": "1960", "in_stock": False}
}

play_with_library()