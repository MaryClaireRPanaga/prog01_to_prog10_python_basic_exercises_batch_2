# Program to find the lowest number until invalid input

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        numbers.append(num)
    except:
        break  # stop if input is invalid
# display lowest number
if numbers:
    print("Lowest number is:", min(numbers))
else:
    print("No valid input")