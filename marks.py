student_marks={
    "prasanth":92,
    "harry":78,
    "dimpy":56,
    "aniket":99,
    "prem":34
}
student_grade={

}
for student in student_marks:
    marks=student_marks[student]
    if marks>90:
        student_grade[student]="A+"
    elif marks>80:
        student_grade[student] = "B+"
    elif marks>70:
        student_grade[student] = "C+"
    elif marks>60:
        student_grade[student] = "D+"
    elif marks>50:
        student_grade[student] = "E+"
    elif marks>40:
        student_grade[student] = "F"
print(student_grade)