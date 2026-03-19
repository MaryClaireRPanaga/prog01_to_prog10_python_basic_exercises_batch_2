# Program to convert fullname to Pascal Case
fullname = input("Enter your fullname: ")
words = fullname.split()
pascal_case = ''.join([word.capitalize() for word in words])

print(pascal_case)