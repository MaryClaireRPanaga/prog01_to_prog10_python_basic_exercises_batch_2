# Program to display all numbers that have duplicates from 10 inputs
numbers = []
# input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
# display numbers that appear more than once (duplicates)
duplicates = []
for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("Numbers with duplicates:", duplicates)