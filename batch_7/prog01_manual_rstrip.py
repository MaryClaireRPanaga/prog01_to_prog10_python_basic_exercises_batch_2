# Remove trailing spaces without using rstrip()
text = input("Enter a string: ")
end = len(text) - 1
while end >= 0 and text[end] == " ":
    end -= 1
result = text[:end + 1]

print("Output:", result)