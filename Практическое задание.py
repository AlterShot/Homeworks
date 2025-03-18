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
        if average_solo is None:
            print(f"Студент {name} не имеет оценок")
            continue
        status = "Успешен" if average_solo >= 75 else "Неуспешен"
        print(f"Студент: {name}\nСредний балл: {average_solo:.2f}\nСтатус: {status}")


def calculate_average_overall(students):
    all_grades = []
    for student in students:
        all_grades.extend(student["grades"])
    return sum(all_grades) / len(all_grades)


def finding_to_exclude(students):
    students_grades = [student for student in students if student["grades"]]
    student_execute = min(students_grades, key=average_grade)
    if not student_execute["grades"]:
        return
    minimal_grade = calculate_average(student_execute["grades"])
    print(f"Студент с наименьшим баллом: {student_execute["name"]} (Балл: {minimal_grade:.2f}) будет исключен")
    students.remove(student_execute)


def adding_student(students, name, grades):
    students.append({"name": name, "grades": grades})


students = [
    {"name": "Harry", "grades": [11, 22, 33]},
    {"name": "Bob", "grades": [12, 80, 70]},
    {"name": "Mary", "grades": [50, 60, 100]},
    {"name": "Wilson", "grades": [88, 54, 70]},
    {"name": "John", "grades": []},
    {"name": "Alto", "grades": [95, 95, 92]},
    {"name": "Tom", "grades": [61, 44, 98]},
    {"name": "Roxie", "grades": [83, 99, 100]}
]

adding_student(students, "Boris", [100, 90, 100])

announce(students)

average_all = calculate_average_overall(students)

print(f"Общий средний балл: {average_all:.2f}")

finding_to_exclude(students)

print("Новый список: ")
for student in students:
    print(f"{student["name"]}")
