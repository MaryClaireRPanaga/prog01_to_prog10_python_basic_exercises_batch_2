# Program to left-justify a string without using ljust()
s = input("Enter a string: ")
width = int(input("Enter total width: "))
spaces_to_add = width - len(s)
if spaces_to_add > 0:
    s = s + " " * spaces_to_add

print(f"'{s}'")