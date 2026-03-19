# Program to check if string ends with a substring without using endswith()
s = input("Enter a string: ")
ending = input("Enter ending substring: ")

if s[-len(ending):] == ending:
    print(True)
else:
    print(False)