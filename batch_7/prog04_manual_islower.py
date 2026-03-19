# Check if all characters are lowercase
text = input("Enter a string: ")
is_lower = True
for ch in text:
    if 'A' <= ch <= 'Z':
        is_lower = False
        break

print("Output:", is_lower)