# Count occurrences
text = input("Enter a string: ")
sub = input("Enter substring: ")
count = 0
for i in range(len(text) - len(sub) + 1):
    if text[i:i+len(sub)] == sub:
        count += 1

print("Output:", count)