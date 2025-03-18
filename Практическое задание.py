import sys


def calculate_average(grades):
    if not grades:
        return None
    return sum(grades) / len(grades)


def average_grade(student):
    return calculate_average(student["grades"])


def announce(students):
    for student in students:
        name = student["name"]
        grade = student["grades"]
        if not grade:
            print(f"Студент {name} не имеет оценок")
            continue
        average_solo = calculate_average(grade)
        status = "Успешен" if average_solo >= 75 else "Неуспешен"
        print(f"Студент: {name}\nСредний балл: {average_solo:.2f}\nСтатус: {status}")


def calculate_average_overall(students):
    all_grades = []
    for student in students:
        if not student["grades"]:
            continue
        all_grades.extend(student["grades"])
    return sum(all_grades) / len(all_grades)


def finding_to_exclude(students):
    students_grades = [student for student in students if student["grades"]]
    student_execute = min(students_grades, key=average_grade)
    minimal_grade = calculate_average(student_execute["grades"])
    print(f"Студент с наименьшим баллом: {student_execute["name"]} (Балл: {minimal_grade:.2f}) будет исключен")
    students.remove(student_execute)
    print("Новый список: ")
    for student in students:
        print(f"{student["name"]}")


def adding_student(students, name, grades):
    students.append({"name": name, "grades": grades})


def user_interface():
    while True:
        begin = input(f"Выберите нужную функцию (список с баллами, общий средний, добавление студента, "
                      f"удаление студента с низшим баллом)\nДля выхода введите \"выход\": ").lower()
        if begin == "список с баллами":
            announce(students)
        elif begin == "общий средний":
            average_all = calculate_average_overall(students)
            print(f"Общий средний балл: {average_all:.2f}")
        elif begin == "удаление студента с низшим баллом":
            finding_to_exclude(students)
        elif begin == "добавление студента":
            name = input("Введите имя: ")
            grade = []
            for i in range(3):
                while True:
                    try:
                        grade_input = int(input(f"Введите оценку {i + 1}: "))
                        grade.append(grade_input)
                        break
                    except ValueError:
                        print("Неверный формат. Введите еще раз: ")
            adding_student(students, name, grade)
            print("Новый список: ")
            for student in students:
                print(f"{student["name"]}")
        elif begin == "выход":
            sys.exit()


students = [
    {"name": "Harry", "grades": [11, 22, 33]},
    {"name": "Bob", "grades": [12, 80, 70]},
    {"name": "Mary", "grades": [50, 60, 100]},
    {"name": "Wilson", "grades": [88, 54, 70]}
]

user_interface()
