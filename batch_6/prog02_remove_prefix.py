# Program to remove a prefix without using removeprefix()
s = input("Enter a string: ")
prefix = input("Enter prefix to remove: ")

if s[:len(prefix)] == prefix:
    print(s[len(prefix):])
else:
    print(s)