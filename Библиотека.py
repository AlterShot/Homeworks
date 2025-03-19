def book_list_view(library):
    if not library:
        print("В библиотеке нет книг.")
    else:
        print("Список книг: ")
        for book in library:
            print(book)


library = {
    "Мертвые души": {"author": "Гоголь", "year": "1850", "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": "2024", "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": "1320", "in_stock": True},
    "1984": {"author": "Хаксли", "year": "1960", "in_stock": False}
}

book_list_view(library)
