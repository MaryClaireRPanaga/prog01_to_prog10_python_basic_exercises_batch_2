# Remove suffix without using removesuffix()
text = input("Enter a string: ")
suffix = input("Enter suffix to remove: ")
if text[-len(suffix):] == suffix:
    result = text[:-len(suffix)]
else:
    result = text

print("Output:", result)