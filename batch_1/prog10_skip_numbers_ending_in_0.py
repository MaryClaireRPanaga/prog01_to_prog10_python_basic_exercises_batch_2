# Program to print numbers form 0 to 100 except those ending in 0

# Loop from 0 to 100
for i in range(0, 101):
    # Skip numbers divisible by 10
    if i % 10 != 0:
        print(i)