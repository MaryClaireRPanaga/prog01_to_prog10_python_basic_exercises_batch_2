# Check starting substring
text = input("Enter a string: ")
prefix = input("Enter prefix: ")

if text[:len(prefix)] == prefix:
    print("Output: True")
else:
    print("Output: False")