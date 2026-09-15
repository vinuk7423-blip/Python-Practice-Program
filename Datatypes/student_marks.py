subjects = ("os","c","c++")
marks = {
    "os":74,
    "c":83,
    "c++":65
}
total =sum(marks.values())
average = total / len(subjects)
print("subjects:",subjects)
print("marks:",marks)
print("total marks:",total)
print("Average Marks:",average)