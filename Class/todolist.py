class ToDoList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, task):
        check_task = task.strip().lower()

        if check_task not in self.tasks:
            self.tasks[check_task] = {"status": False}
            print(f"Задача \"{task}\" добавлена")
        else:
            print(f"Задача \"{task}\" уже существует")

    def complete_task(self, task):
        check_task = task.strip().lower()

        if check_task in self.tasks:
            if not self.tasks[check_task]["status"]:
                self.tasks[check_task]["status"] = True
                print(f"Задача \"{task}\" отмечена выполненной")
            else:
                print(f"Задача \"{task}\" уже выполнена")
        else:
            print(f"Задача не найдена")

    def remove_task(self, task):
        check_task = task.strip().lower()

        if check_task in self.tasks:
            del self.tasks[check_task]
            print(f"Задача \"{task}\" удалена")
        else:
            print(f"Задача не найдена")

    def show_list_tasks(self):
        if not self.tasks:
            print("Задач пока нет.")
        else:
            for task, status in self.tasks.items():
                t_status = "\u2705" if status["status"] else "\u274C"
                print(f"\n{t_status}: {task.capitalize()}")