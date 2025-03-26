from todolist import ToDoList

def get_out():
    return False

def play_with_todolist():
    todolist = ToDoList()
    main_menu = {
        "1": todolist.list_tasks,
        "2": todolist.add_task,
        "3": todolist.remove_task,
        "4": todolist.complete_task,
        "5": get_out()
    }

    flag = True
    while flag:
        option = input("1. Посмотреть список\n2. Добавить дело\n3. Удалить дело"
                       "\n4. Отметить выполненным \n5. Выход\nВаш выбор: ")
        if option == "5":
            flag = get_out()
        elif option == "4":
            task = input("Введите название задачи: ")
            main_menu[option](task)
        elif option in ["2", "3"]:
            task = input("Введите название задачи: ")
            main_menu[option](task)
        elif option == "1":
            main_menu[option]()
        else:
            print("Такого в меню нет.")

play_with_todolist()