def average(values):
    return sum(values) / len(values)


counts = int(input())
students_strings = [input() for _ in range(counts)]

students_grades = {}

for student_string in students_strings:
    student, grade_string = student_string.split(" ")
    grade = float(grade_string)

    if student not in students_grades:
        students_grades[student] = []
    students_grades[student].append(grade)

for student, grades in students_grades.items():
    grades_avg = average(grades)
    grades_formatted = " ".join(f'{grade:.2f}' for grade in grades)
    grades_avg_formatted = f"{grades_avg:.2f}"
    print(f"{student} -> {grades_formatted} (avg: {grades_avg_formatted})")
