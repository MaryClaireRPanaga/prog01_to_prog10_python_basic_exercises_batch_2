# Program to remove leading spaces without using lstrip()
s = input("Enter a string: ")
i = 0
while i < len(s) and s[i] == " ":
    i += 1

print(s[i:])