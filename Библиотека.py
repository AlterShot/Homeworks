def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
        return
    print("Список книг: ")
    for book in library:
        print(book)


def add_book(library, title=None, author=None, year=None):
    if title is None:
        title = input("Введите название книги: ")
    if title in library:
        print(f"\"{title}\" уже существует. Желаете обновить? (да/нет) ")
        option = input().lower()
        if option == "да":
            new_author = input("Укажите нового автора: ")
            try:
                new_year = int(input("Новый год написания: "))
                library[title]["year"] = new_year
            except ValueError:
                print("Год введен некорректно.")
            library[title]["author"] = new_author
            library[title]["in_stock"] = None
            print(f"Информация о книге \"{title}\" успешно обновлена")
        elif option == "нет":
            print("Всего доброго!")
        else:
            print("Введена некорректная команда")
    else:
        if author is None:
            author = input("Укажите автора: ")
        if year is None:
            while True:
                try:
                    year = int(input("Укажите год: "))
                    break
                except ValueError:
                    print("Укажите корректный год: ")

    library[title] = {"author": author, "year": year, "in_stock": None}
    print(f"Книга \"{title}\" добавлена")


library = {
    "Мертвые души": {"author": "Гоголь", "year": "1850", "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": "2024", "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": "1320", "in_stock": True},
    "1984": {"author": "Хаксли", "year": "1960", "in_stock": False}
}

book_list_view(library)
add_book(library)
book_list_view(library)
