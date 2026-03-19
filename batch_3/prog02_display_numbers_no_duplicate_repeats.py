# Program to display numbers, showing duplicates only once

numbers = []
unique_numbers = []
# input 10 numbers
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)
# display only first occurrence
for num in numbers:
    if num not in unique_numbers:
        unique_numbers.append(num)
        print(num)