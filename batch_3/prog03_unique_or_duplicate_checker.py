# Program to check if input is unique or duplicate until invalid input

numbers = []
while True:
    try:
        num = int(input("Enter a number: "))
        
        if num in numbers:
            print("Duplicate")
        else:
            print("Unique")
            numbers.append(num)   
    except:
        break  # stop if input is invalid