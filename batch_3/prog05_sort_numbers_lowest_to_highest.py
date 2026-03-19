# Program to sort numbers from lowest to highest

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break  # stop if input is invalid
# sort and display
numbers.sort()
print("Sorted numbers:", numbers)