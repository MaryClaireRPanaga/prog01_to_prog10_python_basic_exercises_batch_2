# Find first index
text = input("Enter a string: ")
sub = input("Enter substring: ")
index = -1
for i in range(len(text) - len(sub) + 1):
    if text[i:i+len(sub)] == sub:
        index = i
        break

print("Output:", index)