from todolist import ToDoList


def get_out():
    return False


def play_with_todolist():
    todolist = ToDoList()
    main_menu = {
        "1": lambda: todolist.show_list_tasks(),
        "2": lambda: todolist.add_task(input("Введите название задачи: ")),
        "3": lambda: todolist.remove_task(input("Введите название задачи: ")),
        "4": lambda: todolist.complete_task(input("Введите название задачи: "))
    }

    flag = True
    while flag:
        option = input("1. Посмотреть список\n2. Добавить дело\n3. Удалить дело"
                       "\n4. Отметить выполненным \n5. Выход\nВаш выбор: ")
        if option == "5":
            flag = get_out()
        elif option in main_menu:
            main_menu[option]()
        else:
            print("Такого в меню нет.")


play_with_todolist()