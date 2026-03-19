# Program to check if all letters are uppercase without using isupper()
s = input("Enter a string: ")
all_upper = True
for c in s:
    if 'a' <= c <= 'z':
        all_upper = False
        break

print(all_upper)