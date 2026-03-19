# Program to reverse casing of each character
fullname = input("Enter your fullname: ")
reversed_case = ''.join([c.lower() if c.isupper() else c.upper() for c in fullname])

print(reversed_case)