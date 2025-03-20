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


library = {
    "Мертвые души": {"author": "Гоголь", "year": 1850, "in_stock": True},
    "Препятствие - это путь": {"author": "Холидэй", "year": 2024, "in_stock": True},
    "Медитации": {"author": "Аврелий", "year": 1320, "in_stock": True},
    "1984": {"author": "Хаксли", "year": 1960, "in_stock": False}
}

book_list_view(library)

title = input("Введите название книги: ")
author = input("Укажите автора: ")
year = input("Укажите год: ")

while True:
    try:
        year = int(year)
        break
    except ValueError:
        print("Введены некорректные данные. Укажите год: ")
        year = input()

add_book(library, title, author, year)
book_list_view(library)
remove_book(input("Какую книгу удалить? "), library)
book_list_view(library)
issue_book(input("Какую книгу взять? "), library)
for title in library:
    print(f"Книга \"{title}\": {"есть в наличии" if library[title]["in_stock"]
    else "нет в наличии"}")
return_book(input("Какую книгу вернуть? "), library)
for title in library:
    print(f"Книга \"{title}\": {"есть в наличии" if library[title]["in_stock"]
    else "нет в наличии"}")
