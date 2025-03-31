import json


class TaskManager:
    def __init__(self):
        self.tasks = []


    def add_task(self, description: str):
        check_description = description.strip().lower()
        for task in self.tasks:
            if task["description"].strip().lower() == check_description:
                print(f"Задача \"{description.capitalize()}\" уже существует")
                return
        self.tasks.append({"description": description, "completed": False})
        print(f"Задача \"{description.capitalize()}\" добавлена")


    def complete_task(self, index: int):
        index -= 1
        if index < 0 or index >= len(self.tasks):
            print("Задача не найдена")
            return
        task = self.tasks[index]
        if task["completed"]:
            print(f"Задача \"{task["description"]}\" уже выполнена")
        else:
            task["completed"] = True
            print(f"Задача \"{task["description"]}\" отмечена выполненной")


    def remove_task(self, index: int):
        index -= 1
        if index < 0 or index >= len(self.tasks):
            print("Задача не найдена")
            return

        task_to_remove = self.tasks[index]
        del self.tasks[index]
        print(f"Задача \"{task_to_remove["description"]}\"удалена")


    def save_to_json(self, filename: str):
        try:
            task_status = [f"{task["description"]} - {'\u2714' if task['completed'] else '\u274C'}"
                           for task in self.tasks]
            with open(filename, 'w', encoding="utf-8") as file:
                json.dump(task_status, file, ensure_ascii=False)
            print(f"Задачи успешно сохранены в {filename}")
        except Exception as e:
            print(f"Ошибка при сохранении: {e}")


    def load_from_json(self, filename: str):
        try:
            with open(filename, 'r', encoding="utf-8") as file:
                task_status = json.load(file)
            self.tasks = []
            for task in task_status:
                description, status = task.rsplit(' - ', 1)
                completed = True if status == '✔' else False
                self.tasks.append({'description': description, 'completed': completed})
            print(f"Задачи успешно загружены из {filename}")

        except FileNotFoundError:
            print(f"Файл {filename} не найден")
        except json.JSONDecodeError:
            print(f"Ошибка при чтении файла {filename}")
        except Exception as e:
            print(f"Ошибка при загрузке задач: {e}")
