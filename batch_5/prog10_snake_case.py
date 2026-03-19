# Program to convert fullname to snake_case
fullname = input("Enter your fullname: ")
words = fullname.split()
snake_case = '_'.join([word.lower() for word in words])

print(snake_case)