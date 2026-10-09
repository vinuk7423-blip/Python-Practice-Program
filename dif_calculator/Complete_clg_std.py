students = []
while True:
    print("\n================================")
    print("     COLLEGE STUDENT SYSTEM")
    print("================================")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Find Top Student")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("\nEnter student name: ")
        roll_number = int(input("Enter roll number: "))
        print("\nEnter marks out of 100")
        python_marks = float(input("Python: "))
        dbms_marks = float(input("DBMS: "))
        web_marks = float(input("Web Development: "))
        maths_marks = float(input("Mathematics: "))
        english_marks = float(input("English: "))
        total = (
            python_marks
            + dbms_marks
            + web_marks
            + maths_marks
            + english_marks
        )
        average = total / 5
        percentage = (total / 500) * 100
        if percentage >= 90:
            grade = "A+"
        elif percentage >= 80:
            grade = "A"
        elif percentage >= 70:
            grade = "B"
        elif percentage >= 60:
            grade = "C"
        elif percentage >= 40:
            grade = "D"
        else:
            grade = "F"
        if (
            python_marks >= 40
            and dbms_marks >= 40
            and web_marks >= 40
            and maths_marks >= 40
            and english_marks >= 40
        ):
            result = "PASS"
        else:
            result = "FAIL"
        student = {
            "name": name,
            "roll": roll_number,
            "python": python_marks,
            "dbms": dbms_marks,
            "web": web_marks,
            "maths": maths_marks,
            "english": english_marks,
            "total": total,
            "average": average,
            "percentage": percentage,
            "grade": grade,
           "result": result
        }
        students.append(student)
        print("\nStudent added successfully!")
    elif choice == 2:
        if len(students) == 0:
            print("\nNo students available.")
        else:
            print("\n========== STUDENT DETAILS ==========")
            for student in students:
                print("\n----------------------------")
                print("Name:", student["name"])
                print("Roll Number:", student["roll"])
                print("Python:", student["python"])
                print("DBMS:", student["dbms"])
                print("Web Development:", student["web"])
                print("Mathematics:", student["maths"])
                print("English:", student["english"])
                print("Total:", student["total"])
                print("Average:", student["average"])
                print("Percentage:", student["percentage"])
                print("Grade:", student["grade"])
                print("Result:", student["result"])
    elif choice == 3:
        if len(students) == 0:
            print("\nNo students available.")
        else:
            top_student = students[0]
            for student in students:
                if student["percentage"] > top_student["percentage"]:
                    top_student = student
            print("\n===== TOP STUDENT =====")
            print("Name:", top_student["name"])
            print("Roll Number:", top_student["roll"])
            print("Percentage:", top_student["percentage"])
            print("Grade:", top_student["grade"])
    elif choice == 4:
        print("\nThank you for using the system!")
        break
    else:
        print("\nInvalid choice. Please try again.")