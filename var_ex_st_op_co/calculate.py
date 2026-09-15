num1=int(input("enter the first number:"))
operator=(input("Enter operator(+,-,*,/: "))
num2=int(input("enter the second number: "))

if operator == "+":
    result=num1+num2
elif operator == "-":
    result=num1-num2
elif operator == "*":
    result=num1*num2
elif operator == "/":
    if num1 != 0:
        result=num1/num2
    else:
        result="Cannot divide by zero"
else:
    result=("Invalid operator")
print("Result:",result)