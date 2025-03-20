#ask the user to input a number from 0-1000
#store it inside a variable
six_digits = input("Input a number from 0-1000: ")
#add zeros at the beginning until it becomes 6 digits
#print the numbers
if six_digits.isdigit() and 0 <= int(six_digits) <= 1000:
    print(six_digits.zfill(6))
else:
    ("Please enter a number from 0-1000")
