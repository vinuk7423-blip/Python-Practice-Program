number_of_students=int(input("How many students?: "))
for student in range(number_of_students):
    print("/nStudent",student + 1)
    name = input("Enter student name:")
    marks=float(input("Enter marks:"))
    if marks >= 90:
        grade = "A+"
    elif marks >= 80:
        grade = "A"
    elif marks >= 70:
        grade = "B"
    elif marks >= 60:
        grade = "C"
    elif marks >= 40:
        grade = "D"
    else:
        grade= "F"
    print("Nmae:",name)
    print("Marks:",marks)
    print("Grade:",grade)
        