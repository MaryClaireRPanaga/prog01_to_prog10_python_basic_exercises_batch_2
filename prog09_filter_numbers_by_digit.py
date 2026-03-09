# Prog09: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero or ending five.
num = 0
while num <= 100:
    last_digit = num % 10
    #Check if the last digit is NOT 0 AND NOT 5
    if last_digit != 0 and last_digit != 5:
        print(num)
    num += 1