# Program to count number of words in a statement
statement = input("Enter a statement: ")
words = statement.split()

# Split by spaces
print("Number of words:", len(words))