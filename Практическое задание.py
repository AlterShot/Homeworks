def calculate_average(grades):
    return sum(grades) / len(grades)


def announce(students):
    for student in students:
        name = student["name"]
        grade = student["grades"]
        average_solo = calculate_average(grade)
        status = "Успешен" if average_solo >= 75 else "Неуспешен"
        print(f"Студент: {name}\nСредний балл: {average_solo:.2f}\nСтатус: {status}")


def calculate_average_overall(students):
    all_grades = []
    for student in students:
        all_grades.extend(student["grades"])
    return sum(all_grades) / len(all_grades)


def finding_to_exclude(students):
    min_grade = 100
    student_exclude = None
    student_removal = None
    for student in students:
        name = student["name"]
        grade = calculate_average(student["grades"])
        if grade < min_grade:
            min_grade = grade
            student_exclude = student["name"]
            student_removal = student
    print(f"Студент с наименьшим баллом: {student_exclude} (Балл: {min_grade:.2f}) будет исключен")
    if student_removal:
        students.remove(student_removal)

def adding_student(name, grades):
    students.append({"name": name, "grades": grades})


students = [
    {"name": "Harry", "grades": [50, 60, 75]},
    {"name": "Bob", "grades": [12, 80, 70]},
    {"name": "Mary", "grades": [50, 60, 100]},
    {"name": "Wilson", "grades": [88, 54, 70]},
    {"name": "John", "grades": [80, 60, 90]},
    {"name": "Alto", "grades": [95, 95, 92]},
    {"name": "Tom", "grades": [61, 44, 98]},
    {"name": "Roxie", "grades": [83, 99, 100]}
]

adding_student("Boris", [10, 20, 30])

announce(students)

average_all = calculate_average_overall(students)

print(f"Общий средний балл: {average_all:.2f}")

finding_to_exclude(students)

print("Новый список: ")
for student in students:
    print(f"{student["name"]}")
