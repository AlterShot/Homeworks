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
        if not all_grades:
            return None
    return sum(all_grades) / len(all_grades)


def finding_to_exclude(students):
    students_grades = [student for student in students if student["grades"]]
    student_execute = min(students_grades, key=average_grade)
    minimal_grade = calculate_average(student_execute["grades"])
    print(f"Студент с наименьшим баллом: {student_execute["name"]} (Балл: {minimal_grade:.2f}) будет исключен")
    students.remove(student_execute)
    new_list(students)


def new_student():
    name = input("Введите имя: ")
    grade = []
    for i in range(3):
        try:
            grade_input = int(input(f"Введите оценку {i + 1}: "))
            if grade_input > 100 or grade_input < 0:
                grade_input = int(input(f"Недопустимое число. Введите еще раз: "))
            grade.append(grade_input)
            return grade, name
        except ValueError:
            print("Неверный формат. Введите еще раз: ")


def adding_student(students, name, grades):
    students.append({"name": name, "grades": grades})
    new_list(students)


def user_interface():
    while True:
        begin = input(f"1. Просмотр списка баллов 2. Общий средний балл 3. Удаление студента с низшим баллом"
                      f"4. Добавление студента 5. Выход: ")
        if begin == "1":
            announce(students)
        elif begin == "2":
            average_all = calculate_average_overall(students)
            print(f"Общий средний балл: {average_all:.2f}")
        elif begin == "3":
            finding_to_exclude(students)
        elif begin == "4":
            name, grade = new_student()
            adding_student(students, name, grade)
        elif begin == "5":
            break


def new_list(students):
    print("Новый список: ")
    for student in students:
        print(f"{student["name"]}")


students = [
    {"name": "Harry", "grades": [11, 22, 33]},
    {"name": "Bob", "grades": [12, 80, 70]},
    {"name": "Mary", "grades": [50, 60, 100]},
    {"name": "Wilson", "grades": [88, 54, 70]}
]

user_interface()
