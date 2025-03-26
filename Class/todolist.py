class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"do": task, "status": False})

    def complete_task(self, task):
        task_find = False
        for do in self.tasks:
            if do["do"] == task and not do["status"]:
                do["status"] = True
                print(f"Задача \"{task}\" отмечена как выполненная")
                task_find = True
                break
        if not task_find:
            print("Задача не обнаружена")

    def remove_task(self, task):
        task_find = False
        for do in self.tasks:
            if do["do"] == task:
                self.tasks.remove(do)
                print(f"Задача \"{task}\" удалена")
                task_find = True
                break
        if not task_find:
            print("Задача не обнаружена")

    def list_tasks(self):
        if not self.tasks:
            print("Задач пока нет.")
        else:
            for do in self.tasks:
                status = "\u2705" if do["status"] else "\u274C"
                print(f"\n{status}: {do["do"]}")
