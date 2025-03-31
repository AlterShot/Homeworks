from final_manager import TaskManager


def get_out():
    return False


def play_with_manager():
    task_manager = TaskManager()
    main_menu = {
        "1": lambda: task_manager.add_task(input("Название задачи: ")),
        "2": lambda: task_manager.complete_task(correcting_input("Индекс задачи для выполнения: ")),
        "3": lambda: task_manager.remove_task(correcting_input("Индекс задачи для удаления: ")),
        "4": lambda: task_manager.save_to_json(input("Название файла для сохранения: ")),
        "5": lambda: task_manager.load_from_json(input("Название файла для загрузки: "))
    }

    flag = True
    while flag:
        option = input("1. Добавить\n2. Выполнить\n3. Удалить\n4. Сохранить\n5. Загрузить\n"
                       "6. Выход\nВаш выбор: ")
        if option == "6":
            flag = get_out()
        elif option in main_menu:
            main_menu[option]()
        else:
            print("Такого в меню нет.")


def correcting_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Пожалуйста, введите число.")


play_with_manager()