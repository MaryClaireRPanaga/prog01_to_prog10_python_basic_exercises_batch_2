# Program to display numbers that do not have duplicates

numbers = []
# Input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
# Check and display numbers without duplicates
for num in numbers:
    if numbers.count(num) == 1:
        print(num)