# Right justify string
text = input("Enter a string: ")
width = int(input("Enter total width: "))
spaces = width - len(text)
if spaces > 0:
    result = " " * spaces + text
else:
    result = text

print("Output:", result)