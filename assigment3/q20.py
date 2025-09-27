#Q20
students_marks = {
    'BCA101': [60, 70, 75, 80, 85],
    'BCA102': [65, 68, 72, 74, 70],
    'BCA103': [50, 55, 60, 65, 70],
    'BCA104': [90, 92, 94, 96, 98],
    'BCA105': [45, 50, 48, 52, 49]
}

students_percentage = {}

for student_id, marks in students_marks.items():
    total = sum(marks)
    percentage = total / len(marks)
    students_percentage[student_id] = round(percentage, 2)

print(students_percentage)
