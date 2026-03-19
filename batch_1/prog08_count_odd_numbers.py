# Program to count how many odd numbers are entered

count = 0
# Loop 10 times
for i in range(10):
    num = int(input(f"Enter number {i+1}: "))
    # Check if number is odd
    if num % 2 != 0:
        count += 1
# Display result
print("Number of odd numbers:", count)