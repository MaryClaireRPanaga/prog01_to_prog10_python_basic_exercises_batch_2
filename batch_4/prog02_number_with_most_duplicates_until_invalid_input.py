# Program to find the number with the most duplicates until invalid input
numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break  # stop on invalid input

if numbers:
    counts = {n: numbers.count(n) for n in set(numbers)}
    most_dup = max(counts, key=counts.get)
    print("Number with most duplicates:", most_dup)
else:
    print("No valid input")