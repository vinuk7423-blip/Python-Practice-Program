try:
    a = int(input("Enter the first number:"))
    b  = int(input("Enter the second number:"))
    result = a / b
except ZeroDivisionError:
    print("Error:Cannot divided by zero")
except ValueError:
    print("Error:Please enter number only")
else:
    print("Result:",result)
finally:
    print("Program execution completed")                