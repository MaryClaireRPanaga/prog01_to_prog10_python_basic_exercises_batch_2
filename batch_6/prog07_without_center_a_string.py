# Program to center a string without using center()
s = input("Enter a string: ")
width = int(input("Enter total width: "))
total_spaces = width - len(s)
if total_spaces > 0:
    left_spaces = total_spaces // 2
    right_spaces = total_spaces - left_spaces
    s = " " * left_spaces + s + " " * right_spaces

print(f"'{s}'")