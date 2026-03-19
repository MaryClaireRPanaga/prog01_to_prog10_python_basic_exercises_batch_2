# Fill with zeros
text = input("Enter a string: ")
width = int(input("Enter total width: "))
zeros = width - len(text)
if zeros > 0:
    result = "0" * zeros + text
else:
    result = text

print("Output:", result)