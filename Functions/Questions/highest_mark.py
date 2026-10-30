students={"Anu":85,
          "Ravi":92,
          "Priya":78,
          "Kiran":95}
topper=max(students,key=students.get)
print("Topper:",topper)
print("Marks:",students[topper])