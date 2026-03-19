# Program to convert all letters to lowercase without using lower()
s = input("Enter a string: ")
result = ""
for c in s:
    if 'A' <= c <= 'Z':
        result += chr(ord(c) + 32)
    else:
        result += c

print(result)