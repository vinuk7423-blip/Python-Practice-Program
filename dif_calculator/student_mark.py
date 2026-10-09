name = input("Enter student name: ")
maths = float(input("Enter Maths marks: "))
science = float(input("Enter Science marks: "))
english = float(input("Enter English marks: "))
python = float(input("Enter Python marks: "))
computer = float(input("Enter Computer marks: "))
total = maths + science + english + python + computer
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
if percentage >= 40:
    result = "PASS"
else:
    result = "FAIL"
print("\n----- STUDENT RESULT -----")
print("Student Name:", name)
print("Total Marks:", total)
print("Average:", average)
print("Percentage:", percentage, "%")
print("Grade:", grade)
print("Result:", result)