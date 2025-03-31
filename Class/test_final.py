from final_manager import TaskManager
import os


def testing_manager():
    task_manager = TaskManager()

    task_manager.add_task("Test 1")

    assert len(task_manager.tasks) == 1, "Ошибка, должно быть одно"
    assert task_manager.tasks[0]["completed"] == False, "Ошибка, должно быть не завершено"

    task_manager.complete_task(1)

    assert task_manager.tasks[0]["completed"] == True, "Ошибка, должно быть выполнено"

    task_manager.add_task("Test 2")

    assert len(task_manager.tasks) == 2, "Ошибка, должно быть 2"

    task_manager.remove_task(1)

    assert len(task_manager.tasks) == 1, "Ошибка, должно быть 1"
    assert task_manager.tasks[0]["description"] == "Test 2", "Ошибка, должно быть Test 2"

    file_name = "testing_final.json"
    task_manager.save_to_json(file_name)

    new_task_manager = TaskManager()
    new_task_manager.load_from_json(file_name)

    assert len(new_task_manager.tasks) == 1, "Ошибка, в списке осталась одна задача"
    assert new_task_manager.tasks[0]["description"] == "Test 2", "Ошибка, такой задачи нет"

    os.remove(file_name)


testing_manager()
