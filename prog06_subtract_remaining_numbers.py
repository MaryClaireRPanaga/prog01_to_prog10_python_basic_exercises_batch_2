# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
# Input the first number
result = int(input("Enter number 1: "))
# Input the remaining 9 numbers
for i in range(2,11):
    num = int(input("Enter number {i}: "))
    result -= num # Subtract the current number from the result
print("Result:", result)