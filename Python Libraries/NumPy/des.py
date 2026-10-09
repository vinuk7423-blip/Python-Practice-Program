import numpy as np
marks = np.array([25,28,37,89,90,92])
sorted_marks = np.sort(marks)
descending_marks = sorted_marks[::-1]
print("Original:",marks)
print("Ascending:",sorted_marks)
print("Descending:",descending_marks)