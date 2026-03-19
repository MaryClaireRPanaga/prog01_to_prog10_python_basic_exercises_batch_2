# Program to sort numbers from highest to lowest until invalid input
numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break

# sort descending
numbers.sort(reverse=True)
print("Numbers from highest to lowest:", numbers)