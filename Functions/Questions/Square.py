try:
    num=int(input("Enter a number:"))
    square=num**2
    print("Square:",square)
except ValueError:
    print("Invalid input!Enter an integer.")
