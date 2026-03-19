# Program to divide two numbers and show decimal result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the secong number: "))
# check if denominator is not zero
if num2 != 0:
    print("Quotient is:", num1 / num2)
else:
    print("Cannot divide by zero")