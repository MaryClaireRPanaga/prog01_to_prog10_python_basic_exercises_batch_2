# Program to compute the sum of 10 numbers

total = 0
# Loop 10 times
for i in range(10):
    num = int(input("Enter number {i+1}: "))
    total += num
# display result
print("Total sum is:", total)