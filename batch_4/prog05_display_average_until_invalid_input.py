# Program to compute average of numbers until invalid input
numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

if numbers:
    avg = sum(numbers) / len(numbers)
    print("Average is:", avg)
else:
    print("No valid input")