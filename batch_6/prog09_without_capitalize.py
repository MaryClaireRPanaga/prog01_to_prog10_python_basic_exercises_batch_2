# Program to capitalize first letter without using capitalize()
s = input("Enter a string: ")
result = ""
if len(s) > 0:
    # FIRST LETTER (this is the important part!)
    first = s[0]
    if 'a' <= first <= 'z':
        result += chr(ord(first) - 32)
    else:
        result += first
    # REST → lowercase
    for c in s[1:]:
        if 'A' <= c <= 'Z':
            result += chr(ord(c) + 32)
        else:
            result += c

print(result)